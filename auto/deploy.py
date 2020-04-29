import argparse
from   subprocess      import call
from   tuulver.version import bump_major, bump_minor, bump_patch

parser = argparse.ArgumentParser(description='Deploy new version of tuulbachs')
parser.add_argument('--verbose', action='store_true',
                    help='send all output to standard output')
# No need to deploy tuulbachs unless bumping some version number
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--bump_major', action='store_true',
                   help='bump the major portion of the version number')
group.add_argument('--bump_minor', action='store_true',
                   help='bump the minor portion of the version number')
group.add_argument('--bump_patch', action='store_true',
                   help='bump the patch portion of the version number')
args = parser.parse_args()

call('./install_local.sh')

vfile = '../version.yaml'
if args.bump_major:
  bump_major(vfile) 
elif args.bump_minor:
  bump_minor(vfile) 
else:
  bump_patch(vfile) 
