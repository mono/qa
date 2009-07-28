#!/usr/bin/python

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

from asp_net_framework.alltests import *
from authentication.alltests import *
from custom_controls.alltests import *
from data_binding.alltests import *
from handlers.alltests import *
from html_controls.alltests import *
from web_controls.alltests import *
from web_service.alltests import *

if __name__ == '__main__':
    monotesting_main()


# vim:ts=4:expandtab:
