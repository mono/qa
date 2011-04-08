# vim:ts=4:expandtab:
import sys
import unittest
import traceback
import subprocess
import Tkinter, tkMessageBox

sys.path.append('..')
import common.monotesting as mono
from common.monoTestCase import monoTestCase


####################################################################
#
#    winformsTestCase class
#

class winformsTestCase(monoTestCase):
    testcaseid = 0
    command = ''
    global message
    message = ''

    def __init__(self,methodname='runTest'):
        monoTestCase.__init__(self,methodname)
        self.verificationErrors = []

    def setUp(self):
        mono.log("Setting up test case %d" % self.testcaseid)
        self.canRun = self.isTestCaseInTestRun()
        if not self.canRun:
            mono.log("   Test case #%d is not found in the test run.... skipping" % self.testcaseid)
            return

    def runTest(self):
        print "Executing script: %s" % self.command
        i = 'r'
        while i == 'r':
            # This works on osx 10.4
            proc = subprocess.Popen(self.command,shell=True) # This call breaks on my os 11.0 machine. Not sure why. Had to use popen2.Popen() instead
            root = Tkinter.Tk()
            root.withdraw()
            tkMessageBox.showinfo("Test Instructions", self.message)
            proc.wait()
            i = raw_input("Did it pass? (y/n/r/I) ")

        if i == 'n':
            self.verificationErrors.append('Did not pass')




    def tearDown(self):
        if not self.canRun:
            return
        self.updateTestCase(self.verificationErrors)
        self.assertEqual([], self.verificationErrors)

