"""
tuul.py
==================
Top level script for executing tuulbachs features.
"""

import argparse
import os
import sys
from tuulver.version import emit_product_name, emit_version


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    # Guidance: https://stackoverflow.com/a/13790741
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('..')
    return os.path.join(base_path, relative_path)
        
parser = argparse.ArgumentParser()
parser.add_argument('--version', help='output the version of tuul itself',
                    action='store_true')
args = parser.parse_args()
if args.version:
  verYaml = resource_path('version.yaml')
  print(emit_product_name(verYaml) + ' version ' + emit_version(verYaml))
