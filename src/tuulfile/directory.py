"""
directory.py
======================
Provide useful directory manipulation functions
"""
from os import chdir, getcwd, path


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
