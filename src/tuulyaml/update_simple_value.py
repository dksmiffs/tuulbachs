"""
Update a simple top-level value in a YAML file
"""

from pathlib import Path
import ruamel.yaml
from tuulyaml.parse import parse_yaml


# -----
def update_value(inout_path, existing_key, new_value):
    """
    Update existing_key to new_value in the existing inout_path YAML file.
    """
    data = parse_yaml(inout_path)
    data[existing_key] = new_value
    yml = ruamel.yaml.YAML()
    outf = Path(inout_path)
    yml.dump(data, outf)
