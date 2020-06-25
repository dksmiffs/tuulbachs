"""
Project exception class
"""


class TuulError(Exception):
    """
    Class used for exceptions thrown by tuulbachs
    """

    def __init__(self, msg=None):
        """
        Constructor that provides a default error message if one's not given
        """
        if msg is None:
            msg = 'An error occurred in tuulbachs'
        super(TuulError, self).__init__(msg)
