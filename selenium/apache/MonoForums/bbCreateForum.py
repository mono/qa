#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.apache.apacheTestCase import apacheTestCase

class bbCreateForum(apacheTestCase):
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
            sel.click("link=Create new Forum")
            sel.wait_for_page_to_load("30000")
            sel.type("Createeditforum1_CreateEditForm_ForumName", "Mono Forum")
            sel.type("Createeditforum1_CreateEditForm_Description", "This forum is for the discussion of Mono.")
            sel.uncheck("//*[@id=\"Createeditforum1_CreateEditForm_Moderated\"]")
            sel.click("//*[@id=\"Createeditforum1_CreateEditForm_CreateUpdate\"]")
            sel.wait_for_page_to_load("30000")
            sel.click("//*[@id=\"NavigationMenu2_ctl00_HomeMenu\"]")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present(""))
            sel.click("//*[@id=\"NavigationMenu2_ctl00_LoginMenu\"]")
            sel.wait_for_page_to_load("30000")

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
