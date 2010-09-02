#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class WebControls_WebRegularExpressionValidator(xsp1TestCase):
    xsp1TestCaseId = 838908
    xsp2TestCaseId = 861816
    xsp4TestCaseId = None

    def test(self):

        if mono.usexsp2 or mono.usexsp4:
            EnterButton = "ctl11"
            ctl4 = "ctl04"
            ctl7 = "ctl07"
            ctl10 = "ctl10"
        else:
            EnterButton = "_ctl11"
            ctl4 = "_ctl4"
            ctl7 = "_ctl7"
            ctl10 = "_ctl10"

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
            sel.click(EnterButton)
            sel.wait_for_page_to_load("30000")
            self.assertEqual("Entered data is valid.", sel.get_text("message"))
            sel.type("year", "200")
            sel.click(EnterButton)
            self.assertEqual("Entered data is valid.", sel.get_text("message"))
            sel.type("year", "20")
            sel.click(EnterButton)
            sel.wait_for_page_to_load("30000")
            self.failIf(sel.is_visible(ctl4))
            sel.type("year", "AD")
            sel.click(EnterButton)
            self.failUnless(sel.is_visible(ctl4))
            sel.type("year", "2002")
            sel.click(EnterButton)
            sel.wait_for_page_to_load("30000")
            sel.type("zipcode", "84606123")
            sel.click(EnterButton)
            self.failUnless(sel.is_visible(ctl7))
            sel.type("zipcode", "846o6123")
            sel.click(EnterButton)
            self.failUnless(sel.is_visible(ctl7))
            sel.type("zipcode", "84606-1234")
            sel.click(EnterButton)
            sel.wait_for_page_to_load("30000")
            self.assertEqual("Entered data is valid.", sel.get_text("message"))
            sel.type("email", "someone#somewhere.com")
            sel.click(EnterButton)
            self.failUnless(sel.is_visible(ctl10))
            sel.type("email", "someone@somewhere")
            sel.click(EnterButton)
            self.assertEqual("invalid format!", sel.get_text(ctl10))
            sel.type("email", "someone@somewhere.edu")
            sel.click(EnterButton)
            sel.wait_for_page_to_load("30000")
            self.failIf(sel.is_visible(ctl4))
            self.failIf(sel.is_visible(ctl7))
            self.failIf(sel.is_visible(ctl10))
            self.assertEqual("Entered data is valid.", sel.get_text("message"))

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
 
