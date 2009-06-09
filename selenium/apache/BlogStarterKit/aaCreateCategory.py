#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.apache.apacheTestCase import apacheTestCase

class aaCreateCategory(apacheTestCase):
    apacheTestCaseId = 867465
    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/BlogStarterKit/Admin")
            sel.type("ctl00_Content_Login1_UserName", "test")
            sel.type("ctl00_Content_Login1_Password", "test")
            sel.click("ctl00_Content_Login1_RememberMe")
            sel.click("ctl00_Content_Login1_LoginButton")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_element_present("link=Manage posts"))
            sel.open("/BlogStarterKit/Admin")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("My Blog"))
            sel.click("link=Manage categories")
            sel.wait_for_page_to_load("30000")
            sel.type("ctl00_Content_NewCategoryForm_NameTextBox", "Technology")
            sel.type("ctl00_Content_NewCategoryForm_DescriptionTextBox", "Technology topics")
            sel.click("ctl00_Content_NewCategoryForm_InsertButton")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Manage categories")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("Technology topics"))

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
