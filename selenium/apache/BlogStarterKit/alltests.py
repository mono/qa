#!/usr/bin/python
import sys

sys.path.append('../../..')
from common.monotesting import *

# sub directories
# Add child test suites to test suite

from aaCreateCategory import *
from ccCreatePost import *

if __name__ == '__main__':
    monotesting_main()

# vim:ts=4:expandtab:
