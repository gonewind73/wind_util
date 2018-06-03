#!/usr/bin/env python3
# coding=utf-8

from setuptools import setup

setup(name='python-windutil',
      py_modules = ["filefolder","logtool"],
      author='gonewind.he',
      author_email='gonewind.he@gmail.com',
      maintainer='gonewind',
      maintainer_email='gonewind.he@gmail.com',
      url='https://github.com/gonewind73/wind_util',
      description='util in python',
      long_description=open('README.rst').read(),
      version='1.0.0',
      python_requires='>=3',
      platforms=["Linux","Windows"],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Networking'])
