#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class HtmlControls_HtmlTextArea(seleniumTestCase):
    testcaseid = 838547

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=htmltextarea")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("Hi there!\nCool!", sel.get_value("myTA"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("myTA", "Hi there!\nCool!\nSome additional text")
        try: self.assertEqual("Hi there!\nCool!\nSome additional text", sel.get_value("myTA"))
        except AssertionError, e: self.verificationErrors.append(str(e))

if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
