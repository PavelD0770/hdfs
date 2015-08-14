#!/usr/bin/env python
# encoding: utf-8

"""HdfsCLI: API and command line interface for HDFS."""

__version__ = '2.0.0'

try:
  from .client import Client, InsecureClient, TokenClient
  from .config import Config
  from .util import HdfsError
except ImportError:
  pass # In setup.py.
