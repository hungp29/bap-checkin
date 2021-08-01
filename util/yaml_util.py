import logging as log
import yaml

# Reads configuration from yaml file
def read_config():
  log.debug('Load config')
  with open('./config.yaml', 'r') as stream:
    try:
      config = yaml.safe_load(stream)
    except Exception as ex:
      log.error('Error in configuration file: config.yaml', exc_info=True)
  
  return config
