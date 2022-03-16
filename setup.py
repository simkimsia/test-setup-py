import re
from codecs import open
from glob import glob
from itertools import chain
from os import path

from setuptools import setup

from demopublicpythonproject import __version__

# get package version
name = "demopublicpythonproject"
here = path.abspath(path.dirname(__file__))

# get package version
version = __version__

if not version:
    raise ValueError("Can't find the version in {name}/__init__.py")


setup(use_scm_version={
    'version_scheme': 'release-branch-semver',
    # 'local_scheme': 'no-local-version',
})


