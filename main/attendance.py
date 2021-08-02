import pytz
import main.share as share
from main.bemo import Bemo
from datetime import date, datetime
class Attendance:

  def __init__(self):
      self.bemo = Bemo()

  def attend(self):
    today = date.today() #datetime.strptime('20210729', "%Y%m%d").date()
    attendance_today = {}
    # Load attendance list
    attendances = self.bemo.load_attendance()
    if attendances:
      # Look for each record to find the today's attendance
      records = attendances['result']['records']
      for i in range(0, len(records)):
        record = records[i]
        check_in = self.__convert_tz(record['check_in']) #datetime.strptime(record['check_in'] + '+0000', '%Y-%m-%d %H:%M:%S%z').astimezone(pytz.timezone(share.get_timezone()))
        check_out = self.__convert_tz(record['check_out']) #datetime.strptime(record['check_out'] + '+0000', '%Y-%m-%d %H:%M:%S%z').astimezone(pytz.timezone(share.get_timezone()))
        print(f'CI: {check_in}; CO: {check_out}')
        if check_in.date() == today:
          attendance_today = record
          break
      
      # If today's attendance exists then execute checkout
      if attendance_today:
        print('Check out')
        attendance = self.bemo.attendance_manual()
        check_in = self.__convert_tz(attendance['check_in'])
        check_out = self.__convert_tz(attendance['check_out'])
        print(f'CI: {check_in}; CO: {check_out}')
      # Otherwise doing checkin
      else:
        print('Check in')
        attendance = self.bemo.attendance_manual()
        check_in = self.__convert_tz(attendance['check_in'])
        check_out = self.__convert_tz(attendance['check_out'])
        print(f'CI: {check_in}; CO: {check_out}')

  def __convert_tz(self, time_str):
    return datetime.strptime(time_str + '+0000', '%Y-%m-%d %H:%M:%S%z').astimezone(pytz.timezone(share.get_timezone()))
