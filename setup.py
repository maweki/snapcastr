from setuptools import setup

setup(
  name='snapcastr',
  packages=['snapcastr'],
  scripts=['bin/snapcastrd'],
  include_package_data=True,
  install_requires=[ 'flask', 'flask_bootstrap', 'flask_nav', 'snapcast', 'wtforms']
)
