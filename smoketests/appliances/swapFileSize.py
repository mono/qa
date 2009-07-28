#!/usr/bin/env python

import sys, unittest, os


filepath = os.path.realpath(__file__)
basepath = os.path.dirname(os.path.dirname(os.path.dirname(filepath)))
#basepath is the absolute path of the trunk/qa directory

sys.path.append(basepath)

import common.monotesting as mono
from smoketests.smokeTestCase import smokeTestCase


class swapFileSize(smokeTestCase):
    vmImageTestCaseId = 546301

    def test(self):
        swapFileSize = self.getFileSize("/swap")
        self.assertEqual(swapFileSize, 536870912)

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
