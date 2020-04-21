"""
update_simple_value.py
================================
Update a simple top-level value in a YAML file
"""

from   pathlib import Path
import ruamel.yaml


# -----
def update_value(inout_path, existing_key, new_value):
  """
  Update existing_key to new_value in the existing inout_path YAML file.
  """
  inf  = Path(inout_path)
  outf = Path(inout_path)

  yml = ruamel.yaml.YAML()
  data = yml.load(inf)

  data[existing_key] = new_value

  yml.dump(data, outf)


# -----
def main():
  # Show example usage
  update_value('../version.yaml', 'version', '0.0.0')


# -----
if '__main__' == __name__:
  main()
