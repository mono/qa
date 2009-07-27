#!/usr/bin/env python
import sys,os

sys.path.append('..')
from common.monotesting import *
from common.helpers import *

# sub directories
# Add child test suites to test suite

from all.alltests import *

# Depending on your OS, import the proper subdirectory
myOS = whichOS()
if myOS == 'win32':
    print "Importing Win32 tests"
    from win32.alltests import *
elif myOS == 'linux':
    print "Importing Linux tests"
    from linux.alltests import *
elif myOS  == 'macos':
    print "Importing Mac OSX tests"
    from macos.alltests import *


if __name__ == '__main__':
    monotesting_main()


# vim:ts=4:expandtab:
