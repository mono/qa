#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase


class CustomControls_RegisterTest(xsp1TestCase):
    xsp1TestCaseId = 837902
    xsp2TestCaseId = 861725
    xsp4TestCaseId = None

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=tabcontrol")
            sel.wait_for_page_to_load("30000")
            sel.click("submit")
            sel.wait_for_page_to_load("30000")

            try:
                if not mono.usexsp2:
                    monoProjectXPath = "//form[@id='_ctl1']/table[2].0.1"
                else:
                    monoProjectXPath = "//form[@id='ctl01']/table[2].0.1"

                self.assertEqual("Mono Project", sel.get_table(monoProjectXPath))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

            sel.type("name", "Google")
            sel.type("url", "http://google.com")
            sel.click("submit")
            sel.wait_for_page_to_load("30000")

            try:
                if not mono.usexsp2:
                    googleXPath = "//form[@id='_ctl1']/table[2].0.3"
                else:
                    googleXPath = "//form[@id='ctl01']/table[2].0.3"

                self.assertEqual("Google", sel.get_table(googleXPath))
            except AssertionError, e:
                self.verificationErrors.append(str(e))
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()



# vim:ts=4:expandtab:
