"""
cli_color.py
===============================
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


# -----
def main():
    print(f"{CliColor.HEAD}header{CliColor.ENDC}")
    print(f"{CliColor.GREEN}ok, green{CliColor.ENDC}")
    print(f"{CliColor.WARN}warning{CliColor.ENDC}")
    print(f"{CliColor.FAIL}failblog{CliColor.ENDC}")
    print(f"{CliColor.BOLD}bold{CliColor.ENDC}")


# -----
if '__main__' == __name__:
    main()
