#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class WebControls_WebPlaceHolder(xsp1TestCase):
    xsp1TestCaseId = 839932
    xsp2TestCaseId = 861813
    xsp4TestCaseId = None

    def test(self):
        if mono.usexsp2 or mono.usexsp4:
            ctl2 = "//*[@id=\"ctl02\"]"
        else:
            ctl2 = "//*[@id=\"_ctl2\"]"

        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_placeholder")
            sel.wait_for_page_to_load("30000")
            self.failIf(sel.is_checked(ctl2))
            sel.click(ctl2)
            self.failUnless(sel.is_checked(ctl2))
            sel.click("link=Mono project Home Page")
            sel.wait_for_page_to_load("30000")
            self.assertEqual("Main Page - Mono", sel.get_title())

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
