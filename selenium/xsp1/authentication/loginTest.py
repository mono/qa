#!/usr/bin/env python

import sys, unittest, time, re
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase


class Authentication_LoginTest(xsp1TestCase):
    xsp1TestCaseId = 837262
    xsp2TestCaseId = 861722
    xsp4TestCaseId = None

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=login")
            sel.wait_for_page_to_load("30000")
            sel.type("UserEmail", "jdoe@somewhere.com")
            sel.type("UserPass", "password")

            if mono.usexsp2 or mono.usexsp4:
                loginButtonName = "ctl04"
                loginButtonXPath = "//html/body/form/input"
            else:
                loginButtonName = "_ctl4"
                loginButtonXPath = "//html/body/form/input[2]"

            sel.click(loginButtonName)
            sel.wait_for_page_to_load("30000")
            sel.click("link=Authentication")
            sel.wait_for_page_to_load("30000")

            if mono.usexsp2 or mono.usexsp4:
                signOutButtonName = "ctl02"
                signOutButtonXPath = "//html/body/form/input"
            else:
                signOutButtonName = "_ctl2"
                signOutButtonXPath = "//html/body/form/input[2]"

            try:
                self.assertEqual("Signout", sel.get_value(signOutButtonXPath))
            except AssertionError, e:
                self.verificationErrors.append(str(e))


            sel.click(signOutButtonName)
            sel.wait_for_page_to_load("30000")

            try:
                self.assertEqual("Login", sel.get_value(loginButtonXPath))
            except AssertionError, e:
                self.verificationErrors.append(str(e))
        except AssertionError, e: self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()



# vim:ts=4:expandtab:
