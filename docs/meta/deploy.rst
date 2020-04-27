deploy
======
Guidance about how to deploy updates to tuulbachs itself

#. Follow :doc:`install` guidance
#. Decide which type of `semantic version <https://semver.org/>`_ upgrade this is (major, minor, patch, etc.)
#. From ``tuulver/version.py``, use the appropriate ``bump_*`` function to update the version string in ``version.yaml``
#. Commit the version change to Git
#. From ``tuuldevops/tag_current_version.py``, use the ``tag_product_version`` function to properly tag this release
#. Push the Git update (including tags) to this repo's remotes
