#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.apache.apacheTestCase import apacheTestCase

class be_0700_addCategoryAsMonoUserTest(apacheTestCase):
    apacheTestCaseId = 875594
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
            sel.click("//a/span[text()='Categories']")
            sel.wait_for_page_to_load("30000")
            for i in range(60):
                try:
                    if sel.is_element_present("//input[@id='ctl00_cphAdmin_txtNewCategory']"): break
                except: pass
                time.sleep(1)
            else: self.fail("time out")
            sel.type("//input[@id='ctl00_cphAdmin_txtNewCategory']", "Mono")
            sel.type("ctl00_cphAdmin_txtNewNewDescription", "All about Mono.  See http://www.mono-project.com")
            sel.click("ctl00_cphAdmin_btnAdd")
            for i in range(60):
                try:
                    if sel.is_element_present("//*[@id=\"ctl00_cphAdmin_grid\"]/*/tr/td[2 and contains(text(), 'Mono')]"): break
                except: pass
                time.sleep(1)
            else: self.fail("time out")
            sel.click("link=Logout")

        except Exception,e:
            self.verificationErrors.append(str(e))

if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
