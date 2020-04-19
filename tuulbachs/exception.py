"""
exceptions.py
==========================
This module contains the set of tuulbachs' exceptions.
"""
import os


class TuulError(Exception):
  """
  The parent exception from which all other Tuulbachs Python exceptions are
  derived.
  """

  def __init__(self, msg=None):
    if msg is None:
      msg = 'An error occurred in tuulbachs'
    super(TuulError, self).__init__(msg)
