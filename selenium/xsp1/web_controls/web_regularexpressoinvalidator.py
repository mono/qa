#!/usr/bin/env python

import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase
import unittest, time, re

class WebControls_WebRegularExpressionValidator(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 838908
        else:
            self.testcaseid = 861816

    def test(self):
        if not self.canRun:
            return
        try:
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

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
 
