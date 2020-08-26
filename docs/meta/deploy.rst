deploy
======
How to deploy updates to tuulbachs itself.

Prerequisite:  User must have already followed :doc:`install` guidance at least once in the target environment.

#. Decide which type of `semantic version <https://semver.org/>`_ upgrade this is (major, minor, patch, etc.)
#. From ``tuulver/version.py``, use the appropriate ``bump_*`` function to update the version string in ``version.yaml``
#. Follow :doc:`install` guidance
#. Commit changes to Git
#. From ``tuuldevops/tag_current_version.py``, use the ``tag_product_version`` function to properly tag this release
#. Push the Git update (including tags) to this repo's remotes
#. In a temp dir, `download all required packages <https://stackoverflow.com/a/14447068>`_ without installing them, tar and zip these for deployment.
#. On an available machine with the `oldest version of GLIBC <https://stackoverflow.com/questions/17654363/pyinstaller-glibc-2-15-not-found>`_ that you wish to support, in the src dir, run ``pyinstaller --add-data ../version.yaml:. --onefile tuul.py``
#. Publish the release (including offline packages tarball and ``tuul`` executable) on the repo's remote (Github, for instance)
