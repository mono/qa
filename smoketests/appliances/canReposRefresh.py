#!/usr/bin/env python

import sys, unittest, os

filepath = os.path.realpath(__file__)
basepath = os.path.dirname(os.path.dirname(os.path.dirname(filepath)))
#basepath is the absolute path of the trunk/qa directory

sys.path.append(basepath)

import common.monotesting as mono
from smoketests.smokeTestCase import smokeTestCase


class canReposRefresh(smokeTestCase):
    vmImageTestCaseId = 546327

    def test(self):
        self.canZypperReposBeRefreshed()

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
