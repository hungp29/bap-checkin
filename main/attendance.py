import pytz
from main.bemo import Bemo
from datetime import date, datetime
from util.file_util import load_user_info

class Attendance:

  def __init__(self):
      self.bemo = Bemo()
      self.user_info = load_user_info()
      if self.user_info:
        self.tz = self.user_info['user_context']['tz']

  def check_in(self):
    today = date.today() #datetime.strptime('20210729', "%Y%m%d").date()
    attendance_today = {}
    # Load attendance list
    attendances = self.bemo.load_attendance()
    if attendances:
      # Look for each record to find the today's attendance
      records = attendances['result']['records']
      for i in range(0, len(records)):
        record = records[i]
        check_in = datetime.strptime(record['check_in'] + '+0000', '%Y-%m-%d %H:%M:%S%z').astimezone(pytz.timezone(self.tz))
        check_out = datetime.strptime(record['check_out'] + '+0000', '%Y-%m-%d %H:%M:%S%z').astimezone(pytz.timezone(self.tz))
        
        if check_in.date() == today:
          attendance_today = record
          break
      
      # If today's attendance exists then execute checkout
      if attendance_today:
        print('Check out')
      # Otherwise doing checkin
      else:
        print('Check in')
