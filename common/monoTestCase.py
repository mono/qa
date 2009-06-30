
import sys
import os
import unittest
import pdb

import monotesting as mono


class monoTestCase(unittest.TestCase):

    def __init__(self,methodname="runTest"):
        unittest.TestCase.__init__(self,methodname)
        self.verificationErrors = []
        self.testcaseid = 0

    #----------------------------------------------------------------------
    def isTestCaseInTestRun(self):
        print "Deprecated call: monoTestCase.isTestCaseInTestRun()"
        return True

    #----------------------------------------------------------------------
    def updateTestCase(self,errorsList):
        print "Deprecated call to monoTestCase.updateTestCase()"

# vim:ts=4:expandtab:
