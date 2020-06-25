"""
Git tag the commit on the current branch with the current version of this
software
"""

from tuulgit.tag_commit import tag_current_signed
from tuulver.version import emit_version


# -----
def tag_product_version(conf_filename):
    """
    Git tag the commit on the current branch with the version of this software
    given in conf_filename
    """
    tag_current_signed(emit_version(conf_filename))
