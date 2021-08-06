import os
import logging as log
import logging.config
import yaml
import http.client


httpclient_logger = log.getLogger('http.client')

# Load logging configuration
def setup_logging(path='./logging.yaml'):
  if not os.path.exists('logs'):
    os.makedirs('logs')
  try:
    with open(path, 'r') as stream:
      config = yaml.safe_load(stream.read())
      logging.config.dictConfig(config)
      log.debug('Completed logging configuration')
  except Exception as ex:
    print('Error in loggin configuration, so using default config')
    print(ex)

    log.basicConfig(filename='logs/bemo.log',\
      format='%(asctime)s - [%(levelname)7s] - %(name)s - %(message)s',\
      level=log.DEBUG,\
      encoding='utf8')
    log.debug('[Default] Completed logging configuration')
  
  httpclient_logging_patch()

# Http client logging
def httpclient_logging_patch(level=log.DEBUG):
  '''Enable HTTPConnection debug logging to the logging framework'''

  def httpclient_log(*args):
      httpclient_logger.log(level, ' '.join(args))

  # mask the print() built-in in the http.client module to use
  # logging instead
  http.client.print = httpclient_log
  # enable debugging
  http.client.HTTPConnection.debuglevel = 1
