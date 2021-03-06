#!/usr/bin/python

import sys
import os
import unittest
import traceback

basepath = os.path.dirname(os.path.realpath(__file__))
while not os.path.isfile(os.path.join(basepath,'common','monoTestCase.py')):
    basepath = os.path.dirname(basepath)
if not basepath in sys.path:
    sys.path.append(basepath)

import common.monotesting as mono
from smoketests.smokeTestCase import smokeTestCase

from installedFilesTest_filelist import *


####################################################################
#
#    xsp1TestCase class
#

class linuxInstalledFilesTestCase(smokeTestCase):
    testcaseid = 875244

    def testSymlinks(self):
        self.checkForSymlinks(symlinks)

    def testFiles(self):
        self.checkForFiles(files)

if __name__ == '__main__':
    mono.monotesting_main()



# vim:ts=4:expandtab:
