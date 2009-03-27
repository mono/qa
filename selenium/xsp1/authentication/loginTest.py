#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class Authentication_LoginTest(seleniumTestCase):
    testcaseid = 837598

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
            sel.click("_ctl4")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Authentication")
            sel.wait_for_page_to_load("30000")

            try:
                self.assertEqual("Signout", sel.get_value("//html/body/form/input[2]"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

            sel.click("_ctl2")
            sel.wait_for_page_to_load("30000")

            try:
                self.assertEqual("Login", sel.get_value("//html/body/form/input[2]"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))
        except AssertionError, e: self.verificationErrors.append(str(e))


if __name__ == "__main__":
    monotesting_main()



# vim:ts=4:expandtab:
