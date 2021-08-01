import logging as log
import logging.config
import yaml

# Load logging configuration
def setup_logging(path='./logging.yaml'):
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
