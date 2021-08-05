import requests
import logging as log
import main.share as share
from main.request_payload import RequestPayload

#--------------
# Bemo Status
#--------------
class BemoStatus:

  def __init__(self):
    self.payload_helper = RequestPayload()
    self.config = share.config

  def check_status(self, session, user_info):
    log.debug('Check status')
    im_status = {}
    # build request payload
    payload, payload_id = self.payload_helper\
      .model('ir.ui.menu')\
      .method('load_menus_root')\
      .args([])\
      .user_info(user_info)\
      .add_context({'website_id': 1})\
      .build(True)
    # send post request to check status
    response = requests.post(self.config['url']['im-status-url'], json=payload, cookies=session)
    if response.status_code == 200:
      im_status = response.json()

    return not 'error' in im_status
