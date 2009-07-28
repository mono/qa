#!/usr/bin/env python
import sys
import os

basepath = os.path.dirname(os.path.realpath(__file__))
while not os.path.isfile(os.path.join(basepath,'common','monoTestCase.py')):
    basepath = os.path.dirname(basepath)
if not basepath in sys.path:
    sys.path.append(basepath)

from common.monotesting import *

# sub directories
# Add child test suites to test suite
from gmcsTest import *
from gmcs2Test import *
from gmcsBitmapTest import *
from visualBasicTest import *
from gacutilTest import *
from pkgVersionsTest import *

if __name__ == '__main__':
    monotesting_main()


# vim:ts=4:expandtab:
