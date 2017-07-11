#!/usr/bin/env python

from distutils.core import setup

setup(name='ledgergrabber',
      version='1.0',
      description='Utils for building prices_db for ledger-cli',
      requires=['requests'],
      packages=['ledgergrabber'])
