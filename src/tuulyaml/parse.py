"""
Parse an input YAML file
"""
from pathlib import Path
import ruamel.yaml


# -----
def parse_yaml(filename):
    """
    Given input path filename, parse YAML file.
    """
    inf = Path(filename)
    yml = ruamel.yaml.YAML()
    return yml.load(inf)
