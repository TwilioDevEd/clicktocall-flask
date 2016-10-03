#!/usr/bin/env python

from setuptools import setup
setup(name='flask-clicktocall',
      version='1.0',
      author='Rob Spectre',
      author_email='deved@twilio.com',
      description='A sample Flask project that implements click to call '
                  'using Twilio.',
      include_package_data=True,
      zip_safe=False,
      packages=['clicktocall', 'tests'],
      license='MIT',
      install_requires=[
          'flask>=0.10',
          'twilio>=6.0.0rc12',
          'tox>=1.7'
      ])
