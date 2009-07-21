#!/usr/bin/python

import sys
import os

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

    def test(self):
        errors = []
        for pkg in pkgs.keys():
            cmd = getPrefix() + pkg
            mono.log("Checking '%s'" % pkg)
            out = executeCmd(cmd)[0]
            if out != pkgs[pkg]:
                errors.append("\t '%s' != '%s'" % (pkg,pkgs[pkg]))

        if len(errors) != 0:
            print "Package versions errors:"
            for err in errors:
                mono.printColor(err,'red')
            self.fail("Package version errors")

if __name__ == '__main__':
    mono.monotesting_main()



# vim:ts=4:expandtab:
