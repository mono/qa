#!/usr/bin/python
import sys

sys.path.append('../..')
from common.monotesting import *

# sub directories
# Add child test suites to test suite
from gmcsTest import *
from gmcs2Test import *
from visualBasicTest import *
from gacutilTest import *
from pkgVersionsTest import *

if __name__ == '__main__':
    monotesting_main()


# vim:ts=4:expandtab:
