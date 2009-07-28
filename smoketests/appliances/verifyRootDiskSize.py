#!/usr/bin/env python

import sys, unittest, os

basepath = os.path.dirname(os.path.realpath(__file__))
while not os.path.isfile(os.path.join(basepath,'common','monoTestCase.py')):
    basepath = os.path.dirname(basepath)
if not basepath in sys.path:
    sys.path.append(basepath)

import common.monotesting as mono
from smoketests.smokeTestCase import smokeTestCase


class verifyRootDiskSize(smokeTestCase):
    testcaseid = 546325

    def test(self):
        mntPoint = "/"
        expectedSize = 30961664
        self.verifyDiskSize(mntPoint, expectedSize)

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
