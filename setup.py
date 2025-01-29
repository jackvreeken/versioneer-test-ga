import sys

from setuptools import find_packages, setup

import versioneer

if sys.version_info < (3, 9):
    sys.exit("Sorry, Python 3.9 or newer is required.")

setup(
    name="versioneer-test-ga",
    version=versioneer.get_version(),
    maintainer="Test",
    author="Test",
    description="Test",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    cmdclass=versioneer.get_cmdclass(),
)
