"""
Define colors and font styles for use in CLI output
"""


# Guidance:  https://stackoverflow.com/a/287944
class CliColor:
    """
    Contain the list of colors and font styles
    """
    HEAD = '\033[95m'
    GREEN = '\033[92m'
    WARN = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
