#!/usr/bin/env python

import sys, unittest, os

basepath = os.path.dirname(os.path.realpath(__file__))
while not os.path.isfile(os.path.join(basepath,'common','monoTestCase.py')):
    basepath = os.path.dirname(basepath)
if not basepath in sys.path:
    sys.path.append(basepath)

import common.monotesting as mono
from smoketests.smokeTestCase import smokeTestCase
from common.helpers import executeCmd


class verifyXdmHackIsInPlace(smokeTestCase):
    testcaseid = -1

    def test(self):
        # This tests that the hack fix is in place for bug 528048
        self.verifyFileContainsLine("/etc/init.d/xdm", "# Required-Start:    $remote_fs dbus")
        self.verifyFileContainsLine("/etc/init.d/xdm", "# Required-Stop:     $remote_fs dbus")

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
