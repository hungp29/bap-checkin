import requests
import re
import json
from util.yaml_util import read_config
from util.file_util import write_session, write_user_info, load_session, load_user_info
from main.decorator.session import session
from main.request_payload import RequestPayload

#-------------
# Bemo Class
#-------------
class Bemo:

  # Constructor
  def __init__(self):
      self.config = read_config()
      self.payload_helper = RequestPayload()

  # Load list attendance
  @session
  def load_attendance(self, *args, **kwargs):
    attendances = {}
    cookies = kwargs["session"]
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
