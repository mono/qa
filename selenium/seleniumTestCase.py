# vim:ts=4:expandtab:
import sys
import unittest
import traceback

sys.path.append('..')
import common.monotesting as mono

from common.monoTestCase import monoTestCase
from selenium import selenium


####################################################################
#
#    seleniumTestCase class
#

class seleniumTestCase(monoTestCase):

    def __init__(self,methodname='runTest'):
        monoTestCase.__init__(self,methodname)
        #self.verificationErrors = []

    def setUp(self):
        mono.log("Setting up test case %d" % self.testcaseid)
        self.canRun = self.isTestCaseInTestRun()
        if not self.canRun:
            mono.log("   Test case #%d is not found in the test run.... skipping" % self.testcaseid)
            return

        try:
            self.verificationErrors = []
            url = "%s:%s" % (mono.base_url,self.port)
            mono.log("   Creating test case(base_url='%s',rc_server='%s',url='%s')" % (mono.base_url,mono.rc_server,url))
            self.selenium = selenium(mono.rc_server, mono.rc_port, mono.rc_browser,url)
            self.selenium.start()
        except Exception, e:
            mono.log('-'*60)
            mono.log(traceback.print_exc(file=sys.stdout))
            mono.log('-'*60)
            self.updateTestCase([('setUp: ' + str(e))])
            raise e

    def tearDown(self):
        #print self.failureException
        if not self.canRun:
            return
        self.selenium.stop()
        self.updateTestCase(self.verificationErrors)
        self.assertEqual([], self.verificationErrors)

