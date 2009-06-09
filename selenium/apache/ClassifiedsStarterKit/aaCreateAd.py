#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.apache.apacheTestCase import apacheTestCase

class aaCreateAd(apacheTestCase):
    apacheTestCaseId = 738629
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
            sel.click("//a[@id='ctl00_TopMenuRepeater_ctl01_MenuLink']/span")
            sel.wait_for_page_to_load("30000")
            sel.click("ctl00_Main_PostAdWizard_SubcategoriesList_ctl03_CategoryButton")
            sel.wait_for_page_to_load("30000")
            sel.click("ctl00_Main_PostAdWizard_AdTypeSelection_0")
            sel.type("ctl00_Main_PostAdWizard_TitleTextBox", "iPod Touch 3g 32GB")
            sel.type("ctl00_Main_PostAdWizard_DescriptionTextBox", "Black ipod touch third gen, 32GB")
            sel.type("ctl00_Main_PostAdWizard_PriceTextBox", "200.00")
            sel.type("ctl00_Main_PostAdWizard_LocationDropDown_OtherLocationTextBox", "Salt Lake City")
            sel.select("ctl00_Main_PostAdWizard_NumDaysList", "label=14 days")
            sel.click("ctl00_Main_PostAdWizard_FinishNavContainer_FinishButtonButton")
            sel.wait_for_page_to_load("30000")
            sel.click("//a[@id='ctl00_TopMenuRepeater_ctl02_MenuLink']/span")
            sel.wait_for_page_to_load("30000")
            self.assertEqual("iPod Touch 3g 32GB", sel.get_text("link=iPod Touch 3g 32GB"))
            sel.click("link=iPod Touch 3g 32GB")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("iPod Touch 3g 32GB"))
            self.failUnless(sel.is_text_present("For Sale: $200.00"))
            try: self.assertEqual("Electronics", sel.get_text("ctl00_Main_AdDetails_ctl00_CategoryNameLabel"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            self.failUnless(sel.is_text_present("Black ipod touch third gen, 32GB"))
            sel.click("link=Logout")
            sel.wait_for_page_to_load("30000")

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
