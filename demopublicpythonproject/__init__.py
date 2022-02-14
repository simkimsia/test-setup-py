"""DemoPublicPythonProject is a test project for demoing how to have layered requirements
while using pip-tools and setup.py.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("demo-public-python-project")
except PackageNotFoundError:
    # package is not installed
    __version__ = "0.0.1"


import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())
