"""
Top level script for executing tuulbachs features
"""

import argparse
import os
import sys
from tuuldevops.tag_current_version import tag_product_version
from tuulver.version import bump_major, bump_minor, bump_patch, \
                            emit_product_name, emit_version


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    # Guidance: https://stackoverflow.com/a/13790741
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('..')
    return os.path.join(base_path, relative_path)


parser = argparse.ArgumentParser()
parser.add_argument('--version',
                    help='output local product\'s version',
                    action='store_true')
parser.add_argument('--bump',
                    choices=('major','minor','patch'),
                    dest='bumpchoice',
                    help='bump a portion of the local product\'s version')
parser.add_argument('--autotag',
                    help='Git tag with local product\'s current version',
                    action='store_true')
args = parser.parse_args()

verYaml = resource_path('version.yaml')
if args.version:
    print(emit_product_name(verYaml) + ' version ' + emit_version(verYaml))
elif args.bumpchoice:
    if ('major' == args.bumpchoice):
        bump_major(verYaml)
    elif ('minor' == args.bumpchoice):
        bump_minor(verYaml)
    elif ('patch' == args.bumpchoice):
        bump_patch(verYaml)
elif args.autotag:
    tag_product_version(verYaml)
