import yaml


# -----
def parse_yaml(filename):
  file = open(filename, 'r')
  return yaml.load(file, Loader=yaml.FullLoader)


# -----
if '__main__' == __name__:
  cfg = parse_yaml('../version.yaml')
  print('from parsed YAML file, product name ==> ' + cfg['product_name'])
