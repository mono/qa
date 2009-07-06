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

    def __printResults(self,tmpfiles,filetype,expected=True):
        expected = "%s" % (['Unexpected','Missing'][expected])
        print ''
        for f in tmpfiles:
            print "   %s %s: %s" % (expected,filetype,f)
        self.assertEqual(0,len(tmpfiles),"%d %s %ss"% (len(tmpfiles),expected.lower(),filetype))

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
        unexpected = []
        for f in badfiles:
            if os.path.isfile(f):
                unexpected.append(f)
        self.__printResults(unexpected,'file',expected=False)

    def testBadDirs(self):
        unexpected = []
        for d in baddirs:
            if os.path.isdir(d):
                unexpected.append(d)
        self.__printResults(unexpected,'dir',expected=False)

    def testBadSymLinks(self):
        unexpected = []
        for l in badsymlinks:
            if os.path.islink(l):
                unexpected.append(l)
        self.__printResults(unexpected,'symlink',expected=False)

if __name__ == '__main__':
    mono.monotesting_main()



# vim:ts=4:expandtab:
