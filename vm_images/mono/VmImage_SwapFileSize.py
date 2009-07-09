#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../..')
import common.monotesting as mono
from vm_images.vmImageTestCase import vmImageTestCase

class VmImage_SwapFileSize(vmImageTestCase):
    vmImageTestCaseId = 546301

    def testSwapFileSize(self):
        swapFileSize = self.getFileSize("/swap")
        self.assertEqual(swapFileSize, 536870912)

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
