# vim:ts=4:expandtab:
import sys, os
import unittest
import traceback
import subprocess
import Tkinter, tkMessageBox

basepath = os.path.dirname(os.path.realpath(__file__))
while not os.path.isfile(os.path.join(basepath,'common','monoTestCase.py')):
    basepath = os.path.dirname(basepath)
if not basepath in sys.path:
    sys.path.append(basepath)

import common.monotesting as mono
from common.monoTestCase import monoTestCase


####################################################################
#
#    winformsTestCase class
#

class winformsTestCase(monoTestCase):
    testcaseid = 0
    command = ''
    message = ''

    def __init__(self,methodname='runTest'):
        monoTestCase.__init__(self,methodname)
        self.verificationErrors = []
        self.canRun = True # This value is deprecated

    def setUp(self):
        mono.log("Setting up test case %d" % self.testcaseid)
        if not self.canRun:
            mono.log("   Test case #%d is not found in the test run.... skipping" % self.testcaseid)
            return

    def runTest(self):
        print "Executing script: %s" % self.command
        i = 2
        while i == 2:
            # This works on osx 10.4
            proc = subprocess.Popen(self.command,shell=True) # This call breaks on my os 11.0 machine. Not sure why. Had to use popen2.Popen() instead
            root = Tkinter.Tk()
            root.withdraw()
            i = tkMessageBox._show(type='yesno', icon='warning', message=self.message + ' Did it pass?')
            proc.wait()

        if i == 1:
            self.verificationErrors.append('Did not pass')




    def tearDown(self):
        if not self.canRun:
            return
        self.assertEqual([], self.verificationErrors)


