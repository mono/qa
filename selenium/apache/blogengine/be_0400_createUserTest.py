#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.apache.apacheTestCase import apacheTestCase

class be_0400_createUserTest(apacheTestCase):
    apacheTestCaseId = 875591
    def test(self):
        if not self.canRun:
            return
        try:

            sel = self.selenium
            sel.open("/blogengine/")
            sel.click("ctl00_aLogin")
            sel.wait_for_page_to_load("30000")
            sel.type("ctl00_cphBody_Login1_UserName", "admin")
            sel.type("ctl00_cphBody_Login1_Password", "admin")
            sel.click("ctl00_cphBody_Login1_LoginButton")
            sel.wait_for_page_to_load("30000")
            sel.click("//a/span[text()='Users']")
            sel.wait_for_page_to_load("30000")
            sel.type("ctl00_cphAdmin_CreateUserWizard1_ctl02_UserName", "mono user")
            sel.type("ctl00_cphAdmin_CreateUserWizard1_ctl02_Password", "mono")
            sel.type("ctl00_cphAdmin_CreateUserWizard1_ctl02_ConfirmPassword", "mono")
            sel.type("ctl00_cphAdmin_CreateUserWizard1_ctl02_Email", "mono@example.com")
            sel.click("ctl00_cphAdmin_CreateUserWizard1_CustomNavContainer0_StepNextButtonButton")
            sel.wait_for_page_to_load("30000")
            
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
