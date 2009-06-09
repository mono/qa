#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.apache.apacheTestCase import apacheTestCase

class ccUnlistAd(apacheTestCase):
    apacheTestCaseId = 867470
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
            self.failUnless(sel.is_text_present("Welcome, test | Logout"))
            sel.click("//a[@id='ctl00_TopMenuRepeater_ctl02_MenuLink']/span")
            sel.wait_for_page_to_load("30000")
            try: self.assertEqual("iPod Touch 3g 32GB", sel.get_text("link=iPod Touch 3g 32GB"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.click("ctl00_Main_CurrentAdsGrid_ctl02_UnlistButton")
            self.assertEqual("Please confirm that you are unlisting this ad. It will no longer appear among the active listings.", sel.get_confirmation())
            sel.click("//a[@id='ctl00_TopMenuRepeater_ctl02_MenuLink']/span")
            sel.wait_for_page_to_load("30000")
            self.failIf(sel.is_text_present("link=iPod Touch 3g 32GB"))
            sel.click("link=Logout")

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:

