#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../..')
import common.monotesting as mono
from vm_images.vmImageTestCase import vmImageTestCase

class VmImage_IsSwapFileActive(vmImageTestCase):
    vmImageTestCaseId = 546302

    def testIsSwapFileActive(self):
        activeSwapSize = self.getActiveSwapSize()
        self.assertEqual(activeSwapSize, 511)

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
