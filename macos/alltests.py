#!/usr/bin/python
import sys

sys.path.append('..')
from common.monotesting import *

# sub directories
# Add child test suites to test suite
from installedFilesTest import *
from visualBasicTest import *


if __name__ == '__main__':
    monotesting_main()


# vim:ts=4:expandtab:
