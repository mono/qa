#!/usr/bin/python

import sys
import os
import unittest

basepath = os.path.dirname(os.path.realpath(__file__))
while not os.path.isfile(os.path.join(basepath,'common','monoTestCase.py')):
    basepath = os.path.dirname(basepath)
if not basepath in sys.path:
    sys.path.append(basepath)

from common.monotesting import *


from menu1Test import *
from menu2Test import *


if __name__ == '__main__':
    monotesting_main()

# vim:ts=4:expandtab:
