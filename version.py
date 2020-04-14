# tuulbachs emitter for tuulbachs-formatted version.yaml file

from tuulyaml.parse import parse_yaml


_filename = 'version.yaml'


# -----
def emit_product():
  cfg = parse_yaml(_filename)
  return cfg['product_name']


# -----
def emit_version():
  cfg = parse_yaml(_filename)
  return str(cfg['major']) + '.' + str(cfg['minor']) + '.' + str(cfg['patch'])
  

# -----
if '__main__' == __name__:
  print(emit_product() + ' ' + emit_version())
