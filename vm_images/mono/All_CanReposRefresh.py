#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../..')
import common.monotesting as mono
from vm_images.vmImageTestCase import vmImageTestCase

class All_CanReposRefresh(vmImageTestCase):
    vmImageTestCaseId = 546327

    def testCanReposRefresh(self):
        self.canReposRefresh()

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
