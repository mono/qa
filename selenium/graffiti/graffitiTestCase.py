# vim:ts=4:expandtab:
import sys,os
import unittest
import traceback

filepath = os.path.realpath(__file__)
basepath = os.path.dirname(os.path.dirname(os.path.dirname(filepath)))
#basepath is the absolute path of the trunk/qa directory

sys.path.append(basepath)
import common.monotesting as mono
from common.helpers import checkOption
from selenium.seleniumTestCase import seleniumTestCase


####################################################################
#
#    apacheTestCase class
#

class graffitiTestCase(seleniumTestCase):
    testcaseid = 0
    def __init__(self,methodname='test'):
        seleniumTestCase.__init__(self,methodname)
        checkOption(mono.graffiti_port,'graffiti_port')
        self.port = mono.graffiti_port
        self.testcaseid = self.graffitiTestCaseId

def monotesting_main():
    mono.monotesting_main()

