import yaml

# Reads configuration from yaml file
def read_config():
  with open('./config.yaml', 'r') as stream:
    try:
      data = yaml.safe_load(stream)
    except:
      print('Error in configuration file: config.yaml')
  
  return data