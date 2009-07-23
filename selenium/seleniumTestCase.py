# vim:ts=4:expandtab:
import sys
import unittest
import traceback

sys.path.append('..')
import common.monotesting as mono
from common.helpers import checkOption

from common.monoTestCase import monoTestCase
from selenium import selenium


####################################################################
#
#    seleniumTestCase class
#

class seleniumTestCase(monoTestCase):

    def __init__(self,methodname='runTest'):
        monoTestCase.__init__(self,methodname)
        self.verificationErrors = []
        self.canRun = True # This value is deprecated
        checkOption(mono.base_url,'base_url')
        checkOption(mono.rc_server,'rc_server')
        checkOption(mono.rc_port,'rc_port')
        checkOption(mono.rc_browser,'rc_browser')


    def setUp(self):
        mono.log("Setting up test case %s" % self.testcaseid)

        try:
            self.verificationErrors = []
            url = "%s:%s" % (mono.base_url,self.port)
            mono.log("   Creating test case(url='%s',rc_server='%s')" % (url,mono.rc_server))
            mono.log("       selenium(mono.rc_server='%s', mono.rc_port='%s', mono.rc_browser='%s',url='%s')" % (mono.rc_server, mono.rc_port, mono.rc_browser,url))
            self.selenium = selenium(mono.rc_server, mono.rc_port, mono.rc_browser,url)
            self.selenium.start()
        except Exception, e:
            mono.log('-'*60)
            mono.log(traceback.print_exc(file=sys.stdout))
            mono.log('-'*60)
            raise e

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

