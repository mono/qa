#!/usr/bin/python

import sys,os
import unittest
import traceback

filepath = os.path.realpath(__file__)
basepath = os.path.dirname(os.path.dirname(filepath))
#basepath is the absolute path of the trunk/qa directory

sys.path.append(basepath)


import common.monotesting as mono
from common.monoTestCase import monoTestCase
from filelist import *


####################################################################
#
#    xsp1TestCase class
#

class macosTestCase(monoTestCase):
    testcaseid = 0

    def __printResults(self,missing,title):
        for f in missing:
            print "   Missing %s: %s" % (title,f)
        self.assertEqual(0,len(missing),"%d missing %ss"% (len(missing),title))

    def testFiles(self):
        missing = []
        for f in files:
            if not os.path.isfile(f):
                missing.append(f)
        self.__printResults(missing,'file')

    def testDirs(self):
        missing = []
        for d in dirs:
            if not os.path.isdir(d):
                missing.append(d)
        self.__printResults(missing,'dir')

    def testLinks(self):
        missing = []
        for l in symlinks:
            if not os.path.islink(l):
                missing.append(l)
        self.__printResults(missing,'symlink')

    def testBadFiles(self):
        for f in badfiles:
            if os.path.isfile(f):
                self.fail("Existing BAD file: %s" % f)

    def testBadDirs(self):
        for d in baddirs:
            if os.path.isdir(d):
                self.fail("Existing BAD dir: %s" % d)

    def testBadSymLinks(self):
        for l in badsymlinks:
            if os.path.islink(l):
                self.fail("Existing BAD symlink: %s" % l)

if __name__ == '__main__':
    mono.monotesting_main()



# vim:ts=4:expandtab:
