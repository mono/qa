#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_WebRegularExpressionValidator(seleniumTestCase):
    testcaseid =

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=web_regularexpressionvalidator")
        sel.wait_for_page_to_load("30000")
        sel.type("year", "2002")
        sel.type("zipcode", "84606")
        sel.type("email", "someone@somewhere.com")
        sel.click("_ctl11")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Entered data is valid.", sel.get_text("message"))
        sel.type("year", "200")
        sel.click("_ctl11")
        self.assertEqual("Entered data is valid.", sel.get_text("message"))
        sel.type("year", "20")
        sel.click("_ctl11")
        sel.wait_for_page_to_load("30000")
        self.failIf(sel.is_visible("_ctl4"))
        sel.type("year", "AD")
        sel.click("_ctl11")
        self.failUnless(sel.is_visible("_ctl4"))
        sel.type("year", "2002")
        sel.click("_ctl11")
        sel.wait_for_page_to_load("30000")
        sel.type("zipcode", "84606123")
        sel.click("_ctl11")
        self.failUnless(sel.is_visible("_ctl7"))
        sel.type("zipcode", "846o6123")
        sel.click("_ctl11")
        self.failUnless(sel.is_visible("_ctl7"))
        sel.type("zipcode", "84606-1234")
        sel.click("_ctl11")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Entered data is valid.", sel.get_text("message"))
        sel.type("email", "someone#somewhere.com")
        sel.click("_ctl11")
        self.failUnless(sel.is_visible("_ctl10"))
        sel.type("email", "someone@somewhere")
        sel.click("_ctl11")
        self.assertEqual("invalid format!", sel.get_text("_ctl10"))
        sel.type("email", "someone@somewhere.edu")
        sel.click("_ctl11")
        sel.wait_for_page_to_load("30000")
        self.failIf(sel.is_visible("_ctl4"))
        self.failIf(sel.is_visible("_ctl7"))
        self.failIf(sel.is_visible("_ctl10"))
        self.assertEqual("Entered data is valid.", sel.get_text("message"))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
