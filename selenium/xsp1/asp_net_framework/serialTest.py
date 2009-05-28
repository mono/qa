#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase


class AspNetFramework_SerialTest(xsp1TestCase):
    xsp1TestCaseId = 837578
    xsp2TestCaseId = 861579

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
