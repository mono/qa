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

    def setUp(self):
        #print "monoTestCase.setUp()"
        self.canRun = self.isTestCaseInTestRun()
        if not self.canRun:
            return

        try:
            self.verificationErrors = []
            log("Creating test case(base_url='%s',rc_server='%s',xsp1_url='%s')" % (mono.base_url,mono.rc_server,mono.xsp1_url))
            self.selenium = selenium(mono.rc_server, mono.rc_port, mono.rc_browser, mono.xsp1_url)
            #self.selenium = selenium(rc_server, rc_port,rc_browser, xsp1_url)

            self.selenium.start()
        except Exception, e:
            log('-'*60)
            log(traceback.print_exc(file=sys.stdout))
            log('-'*60)
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

