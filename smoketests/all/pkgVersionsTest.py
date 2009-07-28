#!/usr/bin/env python

import sys
import os
import pdb
import re
import string
import subprocess

basepath = os.path.dirname(os.path.realpath(__file__))
while not os.path.isfile(os.path.join(basepath,'common','monoTestCase.py')):
    basepath = os.path.dirname(basepath)
if not basepath in sys.path:
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
    testcaseid = 875243

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
            output = string.join(executeCmd(cmd,stderr=subprocess.STDOUT)).replace('\r ','\n')

            if not re.search("[^.0-9a-zA-Z]*" + exes[exe] + "[^.0-9a-zA-Z]*", output):
                errors.append("\t '%s' expected '%s' got:\n%s\n" % (exe,exes[exe],output))

        if len(errors) != 0:
            print "Executable versions errors:"
            for err in errors:
                printColor(err,'red')
            self.fail("Executable version errors")

if __name__ == '__main__':
    mono.monotesting_main()



# vim:ts=4:expandtab:
