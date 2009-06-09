#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.apache.apacheTestCase import apacheTestCase

class aaCreateLocation(apacheTestCase):
    apacheTestCaseId = 867471
    def test(self):
        if not self.canRun:
            return
        try:

            sel = self.selenium
            sel.open("/ClubWebSite/")
            try: self.failUnless(sel.is_text_present("Login"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.type("ctl00_ContentPlaceHolder1_lv1_Login1_UserName", "test")
            sel.type("ctl00_ContentPlaceHolder1_lv1_Login1_Password", "test")
            sel.click("ctl00_ContentPlaceHolder1_lv1_Login1_RememberMe")
            sel.click("ctl00_ContentPlaceHolder1_lv1_Login1_LoginButton")
            sel.wait_for_page_to_load("30000")
            try: self.failUnless(sel.is_text_present("Hello test"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.click("ctl00_TopNavRepeat_ctl02_HyperLink1")
            sel.wait_for_page_to_load("30000")
            sel.click("ctl00_ContentPlaceHolder1_Addbtn")
            sel.wait_for_page_to_load("30000")
            sel.click("ctl00_ContentPlaceHolder1_FormView1_LocationPicker1_addlocation")
            sel.wait_for_page_to_load("30000")
            sel.type("ctl00_ContentPlaceHolder1_FormView1_titleTextBox", "New Zealand")
            sel.type("ctl00_ContentPlaceHolder1_FormView1_descriptionTextBox", "A beautiful country.")
            sel.type("ctl00_ContentPlaceHolder1_FormView1_TextBox1", "New Zealand")
            sel.type("ctl00_ContentPlaceHolder1_FormView1_TextBox2", "Go south, way south")
            sel.click("ctl00_ContentPlaceHolder1_FormView1_GreenRolloverButton3")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present(""))
            sel.click("ctl00_ContentPlaceHolder1_LoginBanner1_LoginView1_Logoutbtn")
            sel.wait_for_page_to_load("30000")
            sel.click("ctl00_TopNavRepeat_ctl01_HyperLink1")
            sel.wait_for_page_to_load("30000")
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
