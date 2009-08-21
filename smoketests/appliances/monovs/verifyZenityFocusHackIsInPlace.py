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
        numFound = self.howManyTimesDoesFileContainThisLine("/usr/share/zenity/zenity.glade", "<property name=\"focus_on_map\">True</property>")
        self.assertEqual(numFound, 11, "There was only %d focus_on_map lines turned on" % numFound)

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
