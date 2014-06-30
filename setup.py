import sys
if sys.argv[1] == 'develop':
    from setuptools import setup
else:
    from distutils.core import setup

try:
    from wk_publisher import __version__ as version
except ImportError:
    version = '???'

setup(
    name='simpleservices',
    version=version,
    author='Hugo Shi',
    description='utility for running simple services',
    packages=['simpleservices'],
    include_package_data=True,
    package_data={'simpleservices':['*.conf']}
)
