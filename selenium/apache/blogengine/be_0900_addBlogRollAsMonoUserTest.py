#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.apache.apacheTestCase import apacheTestCase

class be_0900_addBlogRollAsMonoUserTest(apacheTestCase):
    apacheTestCaseId = 875596
    def test(self):
        if not self.canRun:
            return
        try:

            sel = self.selenium
            sel.open("/blogengine/")
            sel.click("ctl00_aLogin")
            sel.wait_for_page_to_load("30000")
            sel.type("ctl00_cphBody_Login1_UserName", "mono user")
            sel.type("ctl00_cphBody_Login1_Password", "mono")
            sel.click("ctl00_cphBody_Login1_LoginButton")
            sel.wait_for_page_to_load("30000")
            sel.click("//ul[@id='ctl00_42fcbe7c2c9c440abad965a94472fccc_uxMenu_ulMenu']/li[2]/a/span")
            sel.wait_for_page_to_load("30000")
            sel.type("ctl00_cphAdmin_txtTitle", "Slashdot")
            sel.type("ctl00_cphAdmin_txtDescription", "News that matters")
            sel.type("ctl00_cphAdmin_txtWebUrl", "http://slashdot.org")
            sel.type("ctl00_cphAdmin_txtFeedUrl", "http://rss.slashdot.org/Slashdot/slashdot")
            sel.click("ctl00_cphAdmin_cblXfn_0")
            sel.click("ctl00_cphAdmin_cblXfn_5")
            sel.click("ctl00_cphAdmin_btnSave")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_element_present("link=Slashdot"))
            sel.click("link=Go to front page")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_element_present("link=Slashdot"))

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
