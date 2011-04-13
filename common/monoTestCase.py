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

    def __init__(self,methodname="runTest"):      
        unittest.TestCase.__init__(self,methodname)
        self.verificationErrors = []
        # self.testcaseid = 0

    #----------------------------------------------------------------------
    def isTestCaseInTestRun(self):
        print "Deprecated call: monoTestCase.isTestCaseInTestRun()"
        return True

    #----------------------------------------------------------------------
    def updateTestCase(self,errorsList):
        print "Deprecated call to monoTestCase.updateTestCase()"

    #----------------------------------------------------------------------
    def assertLessThan(self, first, second, msg=None):
        """Fail if the second >= first as determined by the '<' operator.
        """
        if not first < second:
            raise self.failureException, \
                  (msg or '%r >= %r' % (second, first))

    def assertGreaterThan(self, first, second, msg=None):
        """Fail if the second <= first as determined by the '>' operator.
        """
        if not first > second:
            raise self.failureException, \
                  (msg or '%r <= %r' % (second, first))

    def assertLessThanOrEquals(self, first, second, msg=None):
        """Fail if the second > first as determined by the '<=' operator.
        """
        if not first <= second:
            raise self.failureException, \
                  (msg or '%r > %r' % (second, first))

    def assertGreaterThanOrEquals(self, first, second, msg=None):
        """Fail if the second < first as determined by the '>=' operator.
        """
        if not first >= second:
            raise self.failureException, \
                  (msg or '%r < %r' % (second, first))



# vim:ts=4:expandtab:
