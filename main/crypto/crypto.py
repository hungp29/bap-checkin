import main.share as share
import os
import logging as log
from cryptography.fernet import Fernet
from util.yaml_util import save_config

#---------------
# Crypto class
#---------------
class Crypto:

  def __init__(self):
    if not os.path.isdir('keys'):
      log.debug('Create keys folder')
      os.makedirs('keys')

    if not os.path.isfile('keys/key_crypto'):
      log.debug('Generate crypto key')
      # generate key
      self.key = Fernet.generate_key()
      with open('keys/key_crypto', 'wb') as binary_stream:
        # write bytes to file
        binary_stream.write(self.key)
    else:
      with open('keys/key_crypto', 'rb') as binary_stream:
        self.key = binary_stream.read()

  # Encrypt password in config file
  def encrypt_pass(self):
    log.debug('Encrypt password')
    if share.config:
      share.config['user']['password'] = self.encrypt(share.config['user']['password'])
      save_config(share.config)

  # Encrypt value
  def encrypt(self, value:str):
    has_encrypt = False
    try:
      self.decrypt(value)
      has_encrypt = True
    except:
      pass
    if not has_encrypt:
      fernet = Fernet(self.key)
      return fernet.encrypt(value.encode()).decode()
    return value

  # Decrypt value
  def decrypt(self, value):
    fernet = Fernet(self.key)
    return fernet.decrypt(value.encode()).decode()