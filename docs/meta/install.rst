install
=======
Note that tuulbachs is not yet published at PyPi.

#. Set up and activate a Python `virtual environment <https://docs.python.org/3/tutorial/venv.html>`_ at the top level of this project
#. ``python3 -m pip install pip-tools``
#. ``pip-compile``
#. ``pip-compile requirements-dev.in``
#. ``pip-sync requirements.txt requirements-dev.txt``
#. ``cd`` to the local ``auto`` directory
#. ``./install_local.sh``
