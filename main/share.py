from tzlocal import get_localzone

user_info = {}
config = {}

def get_timezone():
  tz = get_localzone().zone
  if user_info:
    tz = user_info['user_context']['tz']

  return tz
