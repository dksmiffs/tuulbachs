deploy
======
How to deploy updates to tuulbachs itself.

Prerequisite:  User must have already followed :doc:`install` guidance at least once in the target environment.

#. Decide which type of `semantic version <https://semver.org/>`_ upgrade this is (major, minor, patch, etc.)
#. In ``src/``, run ``python3 tuul.py --bump {major, minor, patch}``
#. Follow :doc:`install` guidance
#. Commit changes to Git
#. In ``src/``, run ``python3 tuul.py --autotag``
#. Push the Git update (including tags) to this repo's remotes
#. In a temp dir, `download all required packages <https://stackoverflow.com/a/14447068>`_ without installing them, tar and zip these for deployment.
#. On an available machine with the `oldest version of GLIBC <https://stackoverflow.com/questions/17654363/pyinstaller-glibc-2-15-not-found>`_ that you wish to support, in the src dir, run ``pyinstaller --add-data ../version.yaml:. --onefile tuul.py``
#. Publish the release (including offline packages tarball and ``tuul`` executable) on the repo's remote (Github, for instance)
