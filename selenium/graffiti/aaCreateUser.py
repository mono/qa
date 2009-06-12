#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../..')
import common.monotesting as mono
from selenium.graffiti.graffitiTestCase import graffitiTestCase

class graffiti_aa_CreateUser(graffitiTestCase):
    graffitiTestCaseId = None
    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=Login")
            sel.wait_for_page_to_load("30000")
            sel.type("UserName", "admin")
            sel.type("Password", "mono")
            sel.click("login")
            sel.wait_for_page_to_load("30000")
            sel.click("ctl00_UserManagementLink")
            sel.wait_for_page_to_load("30000")
            sel.click("//div[@id='content']/div/div/div[1]/div[1]/div/div[2]")
            sel.wait_for_page_to_load("30000")
            sel.type("ctl00_MainRegion_txtUserName", "mono user")
            sel.type("ctl00_MainRegion_txtEmail", "mono@mono.com")
            sel.type("ctl00_MainRegion_txtPassword", "mono")
            sel.click("ctl00_MainRegion_CreateUser")
            sel.wait_for_page_to_load("30000")
            sel.click("ctl00_MainRegion_Roles_ctl00_role")
            sel.click("ctl00_MainRegion_EditCategory")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Users")
            sel.wait_for_page_to_load("30000")
            self.assertEqual("mono user", sel.get_text("//div[@id='ctl00_MainRegion_Category_List']/ul/li[1]/div/div[1]"))
            sel.click("link=Log Off")
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
