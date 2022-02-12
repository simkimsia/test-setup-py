"""TestSetupPy is a test project for demoing how to have layered requirements
while using pip-tools and setup.py.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("test-setup-py")
except PackageNotFoundError:
    # package is not installed
    pass


import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())
