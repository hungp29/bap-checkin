import logging
import util.logging as log
from main.attendance import Attendance

if __name__ == '__main__':
  # setup logging
  log.setup_logging()
  Attendance().check_in()