import logging as log
import json
import util.constants as CONTS
from jinja2 import Template

# Writes json to file
def write_json(filename, data):
  try:
    with open(filename, 'w') as stream:
      json.dump(data, stream)
  except Exception as ex:
    log.error(f'Error in json file: {filename}', exc_info=True)

# Reads json to dict
def read_json(filename):
  data = {}
  try:
    with open(filename, 'r') as stream:
      data = json.load(stream)
  except Exception as ex:
    log.error(f'Error in json file: {filename}', exc_info=True)
  return data

# Writes session info to json file
def write_session(session):
  log.debug('Write session')
  write_json(CONTS.SESSION_FILE, session)

# Writes user information to json file
def write_user_info(user_info):
  log.debug('Write user information')
  write_json(CONTS.USER_INFO_FILE, user_info)

# Load session
def load_session():
  log.debug('Load session from file')
  return read_json(CONTS.SESSION_FILE)

# Load user information
def load_user_info():
  log.debug('load user information from file')
  return read_json(CONTS.USER_INFO_FILE)

# Read template
def read_template(template):
    with open('main/mail/templates/' + template, 'r', encoding='utf-8') as template_stream:
        template_file_content = template_stream.read()
    return Template(template_file_content)
