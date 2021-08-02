import requests
import logging as log
import main.share as share
from main.decorator.session import session
from main.request_payload import RequestPayload

#-------------
# Bemo Class
#-------------
class Bemo:

  # Constructor
  def __init__(self):
    self.config = share.config
    self.payload_helper = RequestPayload()

  # Load list attendance
  @session
  def load_attendance(self, *args, **kwargs):
    log.debug('Load attendance')
    attendances = {}
    cookies = kwargs['session']
    user_info = kwargs['user_info']
    # build request payload
    payload, payload_id = self.payload_helper\
      .user_info(user_info)\
      .model('hr.attendance')\
      .domain([['employee_id.user_id','=',user_info['user_id']]])\
      .limit(80)\
      .fields([
              'company_id',
              'employee_id',
              'work_location_id',
              'check_in',
              'check_out',
              'worked_hours',
              'schedule_id',
              'hours_arrive_late',
              'hours_leave_soon',
              'paid_work_day',
              'state'
          ])\
      .build()
    # send post request to get attendance list
    response = requests.post(self.config['url']['attendance-list-url'], json=payload, cookies=cookies)
    if response.status_code == 200:
      attendances = response.json()

    return attendances

  # Doing attendance manual
  @session
  def attendance_manual(self, *args, **kwargs):
    log.debug('Doing attendance')
    attendance = {}
    cookies = kwargs['session']
    user_info = kwargs['user_info']
    # build request payload
    payload, payload_id = self.payload_helper\
      .user_info(user_info)\
      .model('hr.employee')\
      .method('attendance_manual')\
      .args([[1675],'hr_attendance.hr_attendance_action_my_attendances'])\
      .build(context_kwargs=True)

    # send post request to do attendance manual
    response = requests.post(self.config['url']['attend-url'], json=payload, cookies=cookies)
    if response.status_code == 200:
      attendance = response.json()['result']['action']['attendance']
    
    return attendance