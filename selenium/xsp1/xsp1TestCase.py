# vim:ts=4:expandtab:
import sys,os
import unittest
import traceback

filepath = os.path.realpath(__file__)
basepath = os.path.dirname(os.path.dirname(os.path.dirname(filepath)))
#basepath is the absolute path of the trunk/qa directory

sys.path.append(basepath)

import common.monotesting as mono
from common.monotesting import log
from common.monoTestCase import monoTestCase
from selenium.seleniumTestCase import seleniumTestCase

log("sys.path = %s" % (str(sys.path))

####################################################################
#
#    xsp1TestCase class
#

class xsp1TestCase(seleniumTestCase):
    testcaseid = 0
    def __init__(self,methodname='test'):
        seleniumTestCase.__init__(self,methodname)
        self.usexsp2 = mono.usexsp2
        if self.usexsp2:
            self.port = mono.xsp2_port
            self.testcaseid = self.xsp2TestCaseId
        else:
            self.port = mono.xsp1_port
            self.testcaseid = self.xsp1TestCaseId

def monotesting_main():
    mono.monotesting_main()

