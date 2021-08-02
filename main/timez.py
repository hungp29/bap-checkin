import pytz
import main.share as share
from datetime import datetime

#--------------
# Class TimeZ
#--------------
class TimeZ:

  def __init__(self):
    pass

  # Convert to timezone
  def convert_tz(self, time_str):
    return datetime.strptime(time_str + '+0000', '%Y-%m-%d %H:%M:%S%z').astimezone(pytz.timezone(share.get_timezone()))