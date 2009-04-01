#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class AspNetFramework_browserCaps(seleniumTestCase):
    testcaseid = 838720

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=browsercaps")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("False", sel.get_text("//table[@id='dg']/tbody/tr[2]/td[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Firefox", sel.get_text("//table[@id='dg']/tbody/tr[6]/td[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("True", sel.get_text("//table[@id='dg']/tbody/tr[19]/td[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("System.Web.UI.HtmlTextWriter", sel.get_text("//table[@id='dg']/tbody/tr[20]/td[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))

if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
