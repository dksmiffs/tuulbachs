"""
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
        """Construct the context manager by storing newPath"""
        self.newPath = path.expanduser(newPath)

    def __enter__(self):
        """
        Enter the context by saving current working directory and then changing
        directories to newPath
        """
        self.savedPath = getcwd()
        chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        """
        Exit the context by changing back to the initial working directory
        """
        chdir(self.savedPath)
