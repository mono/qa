#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_WebCompareValidator(seleniumTestCase):
    testcaseid =

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=web_comparevalidator")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_text_present("Enter twice the same string:"))
        sel.type("Text1", "asdfer adf we")
        sel.type("Text2", "asdfer adf we")
        sel.click("_ctl4")
        sel.wait_for_page_to_load("30000")
        self.failIf(sel.is_visible("//*[@id=\"_ctl3\"]"))
        self.assertEqual("Entered data is valid.", sel.get_text("message"))
        sel.type("Text2", "wrtvasd asdtrqwer")
        sel.click("_ctl4")
        self.failUnless(sel.is_visible("//*[@id=\"_ctl3\"]"))
        sel.type("Text1", "Another test string")
        sel.type("Text2", "Another test string")
        sel.click("_ctl4")
        sel.wait_for_page_to_load("30000")
        self.failIf(sel.is_visible("//*[@id=\"_ctl3\"]"))
        self.assertEqual("Entered data is valid.", sel.get_text("message"))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
