# vim:ts=4:expandtab:
import sys
import unittest
import traceback

sys.path.append('..')
#from common.defaults import *
#from common.monotesting import *
import common.monotesting as mono
from common.monotesting import log

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
        log("\nmonoTestCase.setUp()")
        self.canRun = self.isTestCaseInTestRun()
        if not self.canRun:
            print "Test case #%d is not found in the test run.... skipping" % self.testcaseid
            return

        try:
            self.verificationErrors = []
            url = "%s:%s" % (mono.base_url,self.port)
            log("Creating test case(base_url='%s',rc_server='%s',url='%s')" % (mono.base_url,mono.rc_server,url))
            self.selenium = selenium(mono.rc_server, mono.rc_port, mono.rc_browser,url)
            self.selenium.start()
        except Exception, e:
            log('-'*60)
            log(traceback.print_exc(file=sys.stdout))
            log('-'*60)
            self.updateTestCase([('setUp: ' + str(e))])
            raise e

    def tearDown(self):
        log("monoTestCase.tearDown()")
        #print self.failureException
        if not self.canRun:
            return
        self.selenium.stop()
        self.updateTestCase(self.verificationErrors)
        self.assertEqual([], self.verificationErrors)

