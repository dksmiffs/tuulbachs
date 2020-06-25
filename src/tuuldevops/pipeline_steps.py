"""
Provide routines for outputting automated pipeline steps consistently
"""

from tuulcli.cli_color import CliColor


# -----
def major_step(title, description):
    """
    Output title and description of a major step in the pipeline
    """
    print(f'{CliColor.HEAD}{CliColor.BOLD}{title}: ' +
          f'{CliColor.ENDC}{description}')
