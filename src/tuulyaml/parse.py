"""
parse.py
======================
Parse an input YAML file
"""
from   pathlib import Path
import ruamel.yaml


# -----
def parse_yaml(filename):
  """
  Given input path filename, parse YAML file.
  """
  inf = Path(filename)
  yml = ruamel.yaml.YAML()
  return yml.load(inf)


# -----
if '__main__' == __name__:
  cfg = parse_yaml('../version.yaml')
  print('from parsed YAML file, product name ==> ' + cfg['product_name'])
