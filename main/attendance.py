import requests
from util.yaml_util import read_config
from main.bemo import Bemo

class Attendance:

  def __init__(self):
      self.bemo = Bemo()

  def check_in(self):
    # Load attendance list
    attendances = self.bemo.load_attendance()
    print(attendances)
    # pass