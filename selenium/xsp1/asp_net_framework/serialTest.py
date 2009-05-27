#!/usr/bin/env python


import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class AspNetFramework_SerialTest(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 837578 # xsp1 test case id
        else:
            self.testcaseid = 861579 # xsp2 test case id

    def test(self):
        if not self.canRun:
            return

        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=serial")
            sel.wait_for_page_to_load("30000")

            for ix in range(30):
                if not mono.usexsp2:
                    buttonName = "_ctl2"
                else:
                    buttonName = "ctl02"

                sel.click(buttonName)
                sel.wait_for_page_to_load("30000")

                try:
                    self.assertEqual("Old value: " + str(ix), sel.get_text("//html/body/form/span/b"))
                except AssertionError, e:
                    self.verificationErrors.append(str(e))

        except AssertionError, e:
            self.verificationErrors.append(str(e))

if __name__ == "__main__":
    mono.monotesting_main()



# vim:ts=4:expandtab:
