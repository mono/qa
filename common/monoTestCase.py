#################################################################
#
# Base class for the test cases in the mono testing framework
#
# Author: Rusty Howell (rhowell@novell.com)
#

import sys
import os
import unittest
import pdb

import monotesting as mono


class monoTestCase(unittest.TestCase):
    testcaseid = 0

    def __init__(self,methodname="runTest"):
        unittest.TestCase.__init__(self,methodname)
        self.verificationErrors = []

    #----------------------------------------------------------------------
    def isTestCaseInTestRun(self):
        print "Deprecated call: monoTestCase.isTestCaseInTestRun()"
        return True

    #----------------------------------------------------------------------
    def updateTestCase(self,errorsList):
        print "Deprecated call to monoTestCase.updateTestCase()"

# vim:ts=4:expandtab:
