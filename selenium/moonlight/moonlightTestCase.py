# vim:ts=4:expandtab:
import sys
import unittest
import traceback

sys.path.append('../..')
import common.monotesting as mono
from common.monotesting import log
from common.monoTestCase import monoTestCase
from selenium.seleniumTestCase import seleniumTestCase


####################################################################
#
#    xsp1TestCase class
#

class moonlightTestCase(seleniumTestCase):
    def __init__(self,methodname='runTest'):
        seleniumTestCase.__init__(self,methodname)

