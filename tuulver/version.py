# emitter for tuulbachs-formatted version YAML file

from tuulyaml.parse import parse_yaml


# -----
def emit_product_name(filename):
  cfg = parse_yaml(filename)
  return cfg['product_name']


# -----
def emit_version(filename):
  cfg = parse_yaml(filename)
  return str(cfg['version'])
  

# -----
if '__main__' == __name__:
  fname = '../version.yaml'
  print(emit_product_name(fname) + ' ' + emit_version(fname))
