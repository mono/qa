#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../..')
import common.monotesting as mono
from vm_images.vmImageTestCase import vmImageTestCase

class All_AreRepoRefreshesOff(vmImageTestCase):
    vmImageTestCaseId = 546312

    def testAreRepoRefreshesOff(self):
        self.areRepoRefreshesOff()

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
