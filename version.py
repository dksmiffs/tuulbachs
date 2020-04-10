# tuulbachs emitter for tuulbachs-formatted version.yaml file

import yaml


# -----
def parse_yaml():
  file = open('version.yaml', 'r')
  return yaml.load(file)


# -----
def emit_product():
  cfg = parse_yaml()
  return cfg['product_name']


# -----
def emit_version():
  cfg = parse_yaml()
  return str(cfg['major']) + '.' + str(cfg['minor']) + '.' + str(cfg['patch'])
  

# -----
if "__main__" == __name__:
  print(emit_product() + ' ' + emit_version())
