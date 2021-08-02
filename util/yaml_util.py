import logging as log
import yaml

# Reads configuration from yaml file
def read_config():
  log.debug('Load config')
  with open('./config.yaml', 'r') as stream:
    try:
      config = yaml.safe_load(stream)
    except Exception as ex:
      log.error('Error read configuration file: config.yaml', exc_info=True)
  
  return config

# Writes configuration to yaml file
def save_config(config):
  log.debug('Save config')
  with open('./config.yaml', 'w') as stream:
    try:
      yaml.dump(config, stream, default_flow_style=False)
    except Exception as ex:
      log.error('Error write configuration file: config.yaml', exc_info=True)
