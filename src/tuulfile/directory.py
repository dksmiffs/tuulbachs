"""
directory.py
======================
Provide useful directory manipulation functions
"""
from os import mkdir
from random import randint


# -----
def create_tmp_dir():
    """
    Create a directory under /tmp, return string with full path
    """
    rnd = randint(100000, 999999)
    path = '/tmp/tuulfile_' + str(rnd)
    mkdir(path)
    return path
