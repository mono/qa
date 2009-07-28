#!/usr/bin/python

import sys,os
import unittest
import traceback

filepath = os.path.realpath(__file__)
basepath = os.path.dirname(os.path.dirname(os.path.dirname(filepath)))
#basepath is the absolute path of the trunk/qa directory

sys.path.append(basepath)


import common.monotesting as mono
from smoketests.smokeTestCase import smokeTestCase

from installedFilesTest_filelist import *


####################################################################
#
#    xsp1TestCase class
#

class installedFilesTestCase(smokeTestCase):
    testcaseid = 875244

    def testSymlinks(self):
        self.checkForSymlinks(symlinks)

    def testFiles(self):
        self.checkForFiles(files)

if __name__ == '__main__':
    mono.monotesting_main()



# vim:ts=4:expandtab:
