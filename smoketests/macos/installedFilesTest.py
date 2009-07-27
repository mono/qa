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

from filelist import *


####################################################################
#
#    xsp1TestCase class
#

class installedFilesTestCase(smokeTestCase):
    testcaseid = 0

    #def testFiles(self):
    #    self.checkFiles(files)

    def testSymlinks(self):
        self.checkSymlinksInWindows(symlinks)

    def testFiles(self):
        self.checkFilesInWindows(files)

if __name__ == '__main__':
    mono.monotesting_main()



# vim:ts=4:expandtab:
