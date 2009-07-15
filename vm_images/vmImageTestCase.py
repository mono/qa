# vim:ts=4:expandtab:
import sys
import os
import unittest
import traceback
import pdb

sys.path.append('..')
import common.monotesting as mono
import common.helpers as helpers

from common.monoTestCase import monoTestCase


####################################################################
#
#    vmImageTestCase class
#

class vmImageTestCase(monoTestCase):
    port = 0
    testcaseid = 0

    def __init__(self,methodname='runTest'):
        monoTestCase.__init__(self,methodname)
        self.verificationErrors = []

        cmdOut = helpers.executeCmd("whoami")
        if cmdOut[0].strip() != "root":
            raise Exception("You must run this script as root")
        unittest.TestCase.__init__(self, methodname)

        self.testcaseid = self.vmImageTestCaseId


    def setUp(self):
        mono.log("Setting up test case %s" % self.testcaseid)

        try:
            self.verificationErrors = []
            url = "%s:%s" % (mono.base_url,self.port)
            mono.log("   Creating test case(url='%s',rc_server='%s')" % (url,mono.rc_server))
        except Exception, e:
            mono.log('-'*60)
            mono.log(traceback.print_exc(file=sys.stdout))
            mono.log('-'*60)
            raise e

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)

    def getFileSize(self, filePath):
        statinfo = os.stat(filePath)
        return int(statinfo.st_size)

    def getActiveSwapSize(self):
        cmdOut = helpers.executeCmd("free -m")
        return int(cmdOut[3].split()[1])

    def areRepoRefreshesOff(self):
        cmdOut = helpers.executeCmd("zypper lr")[2:-1]
        for curRefresh in cmdOut:
            self.assertEqual(curRefresh.split()[-1], "No")

    def canReposRefresh(self):
        cmdOut = helpers.executeCmd("zypper ref")[-2].strip()
        self.assertEqual(cmdOut, "All repositories have been refreshed.")
