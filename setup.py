#!/usr/bin/env python


from setuptools import setup

import gron

meta = {}
exec(open('./gron/version.py').read(), meta)

setup(name='gron',
      version=meta['__VERSION__'],
      description='Python library to grep JSON.',
      long_description='This package provides a Python implementation of the original gron written in go',
      keywords='gron json cli',
      author='Bastian Venthur',
      author_email='mail@venthur.de',
      url='https://github.com/venthur/python-gron',
      packages=['gron'],
      entry_points={
          'console_scripts': [
              'gron = gron.__main__:main'
          ]
      },
      license='MIT',
)
