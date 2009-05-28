#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class WebControls_WebImage(xsp1TestCase):
    xsp1TestCaseId = 839928
    xsp2TestCaseId = 861817

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_image")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_element_present("//*[@id=\"im\"]"))

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
