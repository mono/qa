#!/usr/bin/env python


import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class Authentication_LoginTest(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 837262 # xsp1 test case id
        else:
            self.testcaseid = 861722 # xsp2 test case id

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

            if not mono.usexsp2:
                loginButtonName = "_ctl4"
                loginButtonXPath = "//html/body/form/input[2]"
            else:
                loginButtonName = "ctl04"
                loginButtonXPath = "//html/body/form/input"

            sel.click(loginButtonName)
            sel.wait_for_page_to_load("30000")
            sel.click("link=Authentication")
            sel.wait_for_page_to_load("30000")

            if not mono.usexsp2:
                signOutButtonName = "_ctl2"
                signOutButtonXPath = "//html/body/form/input[2]"
            else:
                signOutButtonName = "ctl02"
                signOutButtonXPath = "//html/body/form/input"

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
