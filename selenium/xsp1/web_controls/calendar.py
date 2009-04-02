#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_Calendar(seleniumTestCase):
    testcaseid = 

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=calendar")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Calendar and properties", sel.get_text("//form[@id='_ctl1']/h3"))
        sel.click("link=14")
        sel.wait_for_page_to_load("30000")
        try: self.failUnless(sel.is_text_present("14"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("16"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=16")
        sel.wait_for_page_to_load("30000")
        try: self.failUnless(sel.is_text_present("20"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=20")
        sel.wait_for_page_to_load("30000")
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
