# vim:ts=4:expandtab:
import sys
import unittest
sys.path.append('..')
from common.defaults import *
from common.monotesting import *
from common.monoTestCase import monoTestCase

from selenium import selenium


####################################################################
#
#    seleniumTestCase class
#

class seleniumTestCase(monoTestCase):

    def setUp(self):
        #print "monoTestCase.setUp()"
        self.canRun = self.isTestCaseInTestRun()
        if not self.canRun:
            return

        try:
            self.verificationErrors = []
            self.selenium = selenium(rc_server, rc_port, rc_browser, xsp1_url)
            self.selenium.start()
        except Exception, e:
            #print "monoTestCase.setUp() except"
            msg = re.escape(str(e))
            self.updateTestCase([('setUp: ' + str(e))])
            raise e

    def tearDown(self):
        #print "monoTestCase.tearDown()"
        #print self.failureException
        if not self.canRun:
            return
        self.selenium.stop()
        self.updateTestCase(self.verificationErrors)
        self.assertEqual([], self.verificationErrors)

