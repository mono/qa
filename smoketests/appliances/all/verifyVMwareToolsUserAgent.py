#!/usr/bin/env python

import sys, unittest, os

basepath = os.path.dirname(os.path.realpath(__file__))
while not os.path.isfile(os.path.join(basepath,'common','monoTestCase.py')):
    basepath = os.path.dirname(basepath)
if not basepath in sys.path:
    sys.path.append(basepath)

import common.monotesting as mono
from smoketests.smokeTestCase import smokeTestCase
from common.helpers import *


class verifyVMwareToolsUserAgent(smokeTestCase):
    testcaseid = 871068

    def test(self):
        self.verifyProcessIsRunningAsUser("/usr/bin/vmware-user", "rupert")
        if isMonoVSAppliance():
            expectedPerms = 33261
        else:
            expectedPerms = 35309
        self.verifyFilePermissions("/usr/bin/vmware-user-suid-wrapper", expectedPerms, 0, 0)

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
