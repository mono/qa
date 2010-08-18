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

sys.path.append('..')
from xsp1.alltests import *

from masterpages.alltests import *
from menu.alltests import *
from treeview.alltests import *


if __name__ == '__main__':
    monotesting_main(_usexsp4=True)


# vim:ts=4:expandtab:
