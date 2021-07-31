
import sys
import json
import util.constants as CONTS

# Writes json to file
def write_json(filename, data):
  try:
    with open(filename, 'w') as stream:
      json.dump(data, stream)
  except:
    print(f'Error in json file: {filename}')

# Reads json to dict
def read_json(filename):
  data = {}
  try:
    with open(filename, 'r') as stream:
      data = json.load(stream)
  except:
    print(f'Error in json file: {filename}')
  
  return data

# Writes session info to json file
def write_session(session):
  write_json(CONTS.SESSION_FILE, session)

# Writes user information to json file
def write_user_info(user_info):
  write_json(CONTS.USER_INFO_FILE, user_info)

# Load session
def load_session():
  return read_json(CONTS.SESSION_FILE)

# Load user information
def load_user_info():
  return read_json(CONTS.USER_INFO_FILE)
