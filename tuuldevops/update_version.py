"""
update_version.py
===============================
Update the version in the tuulbachs-formatted YAML version file
"""

from tuulyaml.update_simple_value import update_value


# -----
def update_product_version(conf_filename, new_ver):
  """
  Write a new_ver as the new value for the 'version' key in the conf_filename
  """
  update_value(conf_filename, 'version', new_ver)


# -----
def main():
  # Show example usage
  update_product_version('../version.yaml', '0.0.0')


# -----
if '__main__' == __name__:
  main()
