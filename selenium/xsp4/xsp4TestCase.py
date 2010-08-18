# vim:ts=4:expandtab:

import sys
import os
import unittest
import traceback

basepath = os.path.dirname(os.path.realpath(__file__))
while not os.path.isfile(os.path.join(basepath,'common','monoTestCase.py')):
    basepath = os.path.dirname(basepath)
if not basepath in sys.path:
    sys.path.append(basepath)

import common.monotesting as mono
from common.helpers import checkOption
from selenium.seleniumTestCase import seleniumTestCase


####################################################################
#
#    xsp1TestCase class
#

class xsp4TestCase(seleniumTestCase):
    testcaseid = 0
    port = mono.xsp4_port

    def __init__(self,methodname='test'):
        seleniumTestCase.__init__(self,methodname)
        checkOption(mono.xsp4_port,'xsp4_port')
        self.port = mono.xsp4_port

