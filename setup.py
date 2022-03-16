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

def myversion():
    from setuptools_scm.version import (SEMVER_MINOR, guess_next_simple_semver,
                                        release_branch_semver_version)

    def my_release_branch_semver_version(version):
        v = release_branch_semver_version(version)
        if v == version.format_next_version(guess_next_simple_semver, retain=SEMVER_MINOR):
            return version.format_next_version(guess_next_simple_semver, fmt="{guessed}", retain=SEMVER_MINOR)
        return v

    return {
        'version_scheme': my_release_branch_semver_version,
        'local_scheme': 'no-local-version',
    }


setup(use_scm_version=myversion)


