#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class AspNetFramework_codeBehind1(seleniumTestCase):
    testcaseid = 838721

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=codebehind1")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_text_present("Page Loaded"))
        sel.type("TextBox1", "This is some text")
        sel.click("SubmitButton")
        sel.wait_for_page_to_load("30000")
        try: self.failUnless(sel.is_text_present("This is some text"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
