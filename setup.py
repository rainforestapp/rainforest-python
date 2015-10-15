import os
import sys
import warnings

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))

install_requires = ['requests >= 2.7.0']

# check if mock is present, and install it if needed
try:
    from unittest import mock
except ImportError:
    install_requires += ['mock >= 1.3.0']

if sys.version_info < (2, 7):
    warnings.warn(
        'Python 2.6 is not supported by Rainforest. '
        'If you have any questions, please file an issue on Github or '
        'contact us at help@rainforestqa.com.',
        DeprecationWarning)
    install_requires.append('ssl')

# Get simplejson if we don't already have json
if sys.version_info < (3, 0):
    try:
        import json
    except ImportError:
        install_requires.append('simplejson')

setup(
    name='rainforest',
    cmdclass={'build_py': build_py},
    version='0.0.1',
    description='Rainforest automates your functional and integration testing with our QA-as-a-Service API.',
    author='',
    author_email='help@rainforestqa.com',
    url='https://docs.rainforestqa.com',
    packages=['rainforest', 'rainforest.apibits', 'rainforest.resources', 'rainforest.endpoints', 'rainforest.test'],
    package_data={'rainforest': ['data/ca-certificates.crt', '../VERSION']},
    install_requires=install_requires,
    test_suite='rainforest.test',
    use_2to3=True)
