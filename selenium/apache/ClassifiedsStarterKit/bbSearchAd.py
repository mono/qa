#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.apache.apacheTestCase import apacheTestCase

class aaSearchAd(apacheTestCase):
    apacheTestCaseId = 867467
    def test(self):
        if not self.canRun:
            return
        try:

            sel = self.selenium
            sel.open("/ClassifiedsStarterKit/")
            sel.click("ctl00_LoginView_LoginLink")
            sel.wait_for_page_to_load("30000")
            sel.type("ctl00_Main_LoginConrol_UserName", "test")
            sel.type("ctl00_Main_LoginConrol_Password", "test")
            sel.click("ctl00_Main_LoginConrol_RememberMe")
            sel.click("ctl00_Main_LoginConrol_LoginButton")
            sel.wait_for_page_to_load("30000")
            sel.type("ctl00_SecondBar_CommonSearchTextBox", "iPod")
            sel.click("ctl00_SecondBar_CommonSearchButton")
            sel.wait_for_page_to_load("30000")
            self.assertEqual("iPod Touch 3g 32GB", sel.get_text("link=iPod Touch 3g 32GB"))
            self.failUnless(sel.is_text_present("$200.00"))
            self.failUnless(sel.is_text_present("Salt Lake City"))
            self.failUnless(sel.is_text_present("Electronics"))
            sel.click("link=iPod Touch 3g 32GB")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("Black ipod touch third gen, 32GB"))
            sel.click("link=Logout")
            sel.wait_for_page_to_load("30000")

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:

