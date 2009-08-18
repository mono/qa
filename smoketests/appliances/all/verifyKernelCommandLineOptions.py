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


class verifyKernelCommandLineOptions(smokeTestCase):
    testcaseid = -1

    def test(self):
        appType = whichAppliance()
        if appType == "vmware":
            expectedOptions = ["vga=0x314", "splash=silent"]
        elif appType == "vpc":
            expectedOptions = ["vga=0x314", "splash=silent", "noreplace-paravirt", "i8042.noloop", "clock=pit"]
        elif appType == "livecd":
            raise Exception("Not setup yet")

        self.verifyKernelCommandLineOptions(expectedOptions)

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
