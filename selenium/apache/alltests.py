#!/usr/bin/python
import sys

sys.path.append('../..')
from common.monotesting import *

# sub directories
# Add child test suites to test suite

#from blogengine.alltests import *
#from mojoportal.alltests import *
from BlogStarterKit.alltests import *
from ClassifiedsStarterKit.alltests import *
from ClubWebSite.alltests import *
from MonoForums.alltests import *

if __name__ == '__main__':
    monotesting_main()

# vim:ts=4:expandtab:
