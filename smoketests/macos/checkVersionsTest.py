#!/usr/bin/python

import sys,os
import unittest

filepath = os.path.realpath(__file__)
basepath = os.path.dirname(os.path.dirname(os.path.dirname(filepath)))
#basepath is the absolute path of the trunk/qa directory

sys.path.append(basepath)

import common.monotesting as mono
from common.helpers import *
from smoketests.smokeTestCase import smokeTestCase

from pkgconfig_list import *

####################################################################
#
#    checkVersions class
#

class checkVersionsTestCase(smokeTestCase):
    testcaseid = 0

    def testPkgConfig(self):
        for pkg in pkgconfiglist:
            out = executeCmd('pkg-config --modversion %s' % pkg)
            print out

if __name__ == '__main__':
    mono.monotesting_main()



# vim:ts=4:expandtab:
