#!/usr/bin/python

import sys,os
import unittest
import traceback
import pdb

filepath = os.path.realpath(__file__)
basepath = os.path.dirname(os.path.dirname(filepath))
#basepath is the absolute path of the trunk/qa directory

sys.path.append(basepath)
import common.monotesting as mono
from common.helpers import *
from common.monoTestCase import monoTestCase


####################################################################
#
#    smokeTestCase class
#

class smokeTestCase(monoTestCase):
    testcaseid = 0


    def remove(self,filepath):
        if os.path.exists(filepath):
            os.remove(filepath)

    def __printResults(self,tmpfiles,filetype,expected=True):
        expected = "%s" % (['Unexpected','Missing'][expected])
        if len(tmpfiles) > 0:
            print ''
        for f in tmpfiles:
            print "   %s %s: %s" % (expected,filetype,f)
        self.assertEqual(0,len(tmpfiles),"%d %s %ss"% (len(tmpfiles),expected.lower(),filetype))

    def checkList(self,alist,func,filetype,expected):
        errors = []
        for cur in alist:
            if func(cur) ^ expected:
                errors.append(cur)
        self.__printResults(errors,filetype,expected)

    def checkFiles(self,list):
        self.checkList(list,os.path.isfile,'file',expected=True)

    def checkDirs(self,list):
        self.checkList(list,os.path.isdir,'dir',expected=True)

    def checkSymlinks(self, list):
        self.checkList(list,os.path.islink,'symlink',expected=True)

    def checkUnexpectedFiles(self,list):
        self.checkList(list,os.path.isfile,'file',expected=False)

    def checkUnexpectedDirs(self,list):
        self.checkList(list,os.path.isdir,'dir',expected=False)

    def checkUnexpectedSymlinks(self,list):
        self.checkList(list,os.path.islink,'symlink',expected=False)



# vim:ts=4:expandtab:
