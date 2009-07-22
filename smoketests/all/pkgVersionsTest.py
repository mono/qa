#!/usr/bin/python

import sys
import os
import pdb
import re

filepath = os.path.realpath(__file__)
basepath = os.path.dirname(os.path.dirname(os.path.dirname(filepath)))
#basepath is the absolute path of the trunk/qa directory

sys.path.append(basepath)
import common.monotesting as mono
from smoketests.smokeTestCase import smokeTestCase
from common.helpers import *
from pkgVersionsTest_data import *


####################################################################
#
#    pkgVersionsTestCase class
#

class pkgVersionsTestCase(smokeTestCase):
    testcaseid = 0

    def setUp(self):
        if whichOS() == 'macos':
            pkgs.update(macos_pkgs)
            exes.update(macos_exes)
        if whichOS() == 'linux':
            pkgs.update(linux_pkgs)
            exes.update(linux_exes)
        if whichOS() == 'win32':
            pkgs.update(win32_pkgs)
            exes.update(win32_exes)

    def testPkgConfigFileVersions(self):

        errors = []
        for pkg in pkgs.keys():
            cmd = getPrefix() + pkg
            mono.log("Checking '%s'" % pkg)
            out = executeCmd(cmd)[0].strip()
            if out != pkgs[pkg]:
                errors.append("\t '%s' expected '%s' but got '%s'" % (pkg,pkgs[pkg],out))

        if len(errors) != 0:
            print "Package versions errors:"
            for err in errors:
                printColor(err,'red')
            self.fail("Package version errors")

    def testExecutableFileVersions(self):

        errors = []
        for exe in exes.keys():
            cmd = getPrefix() + exe
            mono.log("Checking '%s'" % exe)
            matched = False
            #pdb.set_trace()
            for curLineWS in executeCmd(cmd):
                curLine = curLineWS.strip()
                if re.search(exes[exe] + " ", curLine):
                    matched = True

            if not matched:
                errors.append("\t '%s' expected '%s'" % (exe,exes[exe]))

        if len(errors) != 0:
            print "Executable versions errors:"
            for err in errors:
                printColor(err,'red')
            self.fail("Executable version errors")

if __name__ == '__main__':
    mono.monotesting_main()



# vim:ts=4:expandtab:
