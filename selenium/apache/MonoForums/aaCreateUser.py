#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.apache.apacheTestCase import apacheTestCase

class aaCreateUser(apacheTestCase):
    apacheTestCaseId = None
    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/AspNetForums/")
            sel.type("Loginbox1_ctl00_username", "admin")
            sel.type("Loginbox1_ctl00_password", "admin")
            sel.click("//*[@id=\"Loginbox1_ctl00_loginButton\"]")
            sel.wait_for_page_to_load("30000")
            sel.click("//*[@id=\"NavigationMenu2_ctl00_HomeMenu\"]")
            sel.wait_for_page_to_load("30000")
            sel.click("//*[@id=\"NavigationMenu2_ctl00_AdminMenu\"]")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Create New Users")
            sel.wait_for_page_to_load("30000")
            sel.type("Createuser1_ctl00_Username", "test")
            sel.type("Createuser1_ctl00_Password", "test")
            sel.type("Createuser1_ctl00_Email", "mono@mono.com")
            sel.click("//*[@id=\"Createuser1_ctl00_CreateAccount\"]")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("User created"))
            sel.click("//*[@id=\"Navigationmenu1_ctl00_LoginMenu\"]")
            sel.wait_for_page_to_load("30000")

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
