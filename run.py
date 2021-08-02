import sys
import util.logging as log
import main.share as share
from main.attendance import Attendance
from main.crypto.crypto import Crypto
from util.yaml_util import read_config

if __name__ == '__main__':
  # setup logging
  log.setup_logging()
  # load config
  share.config = read_config()

  if not 'encryptpass' in sys.argv:
    # doing attendance
    Attendance().attend()
  else:
    # encrypt password
    Crypto().encrypt_pass()