#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase


class WebControls_WebButton(xsp1TestCase):
    xsp1TestCaseId = 839925
    xsp2TestCaseId = 861802
    xsp4TestCaseId = None

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_button")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_element_present("//*[@id=\"btn\"]"))

            for ix in range(5):
                sel.click("btn")
                sel.wait_for_page_to_load("30000")
                self.failUnless(sel.is_element_present("//*[@id=\"btn\"]"))

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
