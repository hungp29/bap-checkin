import requests
import re
import json
import logging as log
import main.share as share
from util.file_util import write_session, write_user_info
from main.crypto.crypto import Crypto

#----------------------
# Bemo Authentication
#----------------------
class BemoAuthen:

  # Constructor
  def __init__(self):
    self.config = share.config
    self.crypto = Crypto()

  # Get csrf token and cookies
  def get_csrf_token_and_cookies(self):
    log.debug('Get CSRF token and cookies')
    # send request to get csrf token and cookies
    response = requests.get(self.config['url']['csrf-token-url'])
    # extract csrf token
    lines = response.text
    if lines:
      lines = lines.split('\n')
      for i in range(0, len(lines)):
        line = lines[i]
        if 'csrf_token' in line:
          csrf_token = line[line.index('"')+1:line.rindex('"')]
          break

    return csrf_token, response.cookies

  # Login and save session
  def login_and_save_session(self):
    log.debug('Login and save session')
    session, user_info = {}, {}
    # call function to get csrf token and cookies
    csrf_token, cookies = self.get_csrf_token_and_cookies()
    # prepare user data to login
    user_data = {'login': self.config['user']['username'], 'password': self.crypto.decrypt(self.config['user']['password']), 'csrf_token': csrf_token}
    # send request to login
    response = requests.post(self.config['url']['login-url'], data=user_data, cookies=cookies)
    # process data after login successfully
    if response.status_code == 200:
      # write session to file
      session = cookies.get_dict() | response.cookies.get_dict()
      write_session(session)
      # extract user information
      lines = response.text
      if lines:
        lines = lines.split('\n')
        for i in range(0, len(lines)):
          line = lines[i]
          if 'odoo.session_info =' in line:
            user_info = json.loads(re.sub('(odoo.session_info =|;)', '', line))
            write_user_info(user_info)
    
    return session, user_info
