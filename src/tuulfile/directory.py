"""
directory.py
======================
Provide useful directory manipulation functions
"""
from os import chdir, getcwd, mkdir, path
from random import randint


# -----
class cd:
    """
    Context manager to change the working directory, from the following source:
       https://stackoverflow.com/a/13197763
    """
    def __init__(self, newPath):
        self.newPath = path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = getcwd()
        chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        chdir(self.savedPath)


# -----
def create_tmp_dir():
    """
    Create a directory under /tmp, return string with full path
    """
    rnd = randint(100000, 999999)
    path = '/tmp/tuulfile_' + str(rnd)
    mkdir(path)
    return path
