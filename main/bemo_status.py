import requests
from main.request_payload import RequestPayload
from util.yaml_util import read_config

#--------------
# Bemo Status
#--------------
class BemoStatus:

  def __init__(self):
    self.payload_helper = RequestPayload()
    self.config = read_config()
    pass

  def check_status(self, session, user_info):
    im_status = {}
    # build request payload
    payload, payload_id = self.payload_helper\
      .partner_ids(user_info['user_id'])\
      .build()
    # send post request to get attendance list
    response = requests.post(self.config['url']['im-status-url'], json=payload, cookies=session)
    if response.status_code == 200:
      im_status = response.json()

    return not 'error' in im_status