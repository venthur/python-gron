#!/usr/bin/env python


from setuptools import setup

meta = {}
exec(open('./gron/version.py').read(), meta)
meta['long_description'] = open('./README.md').read()

setup(name='gron',
      version=meta['__VERSION__'],
      description='Python library to grep JSON.',
      long_description=meta['long_description'],
      long_description_content_type='text/markdown',
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
