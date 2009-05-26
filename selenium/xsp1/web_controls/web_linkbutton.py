#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_WebLinkButton(seleniumTestCase):
    testcaseid = 839930

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=web_linkbutton")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_element_present("//*[@id=\"lb1\"]"))
        self.assertEqual("Click me!", sel.get_text("lb1"))
        self.failUnless(sel.is_element_present("//*[@id=\"lb2\"]"))
        try: self.assertEqual("Remove this link.", sel.get_text("lb2"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("lb2")
        sel.wait_for_page_to_load("30000")
        self.failIf(sel.is_element_present("lb2"))
        self.assertEqual("There used to be a link here, but you have removed it", sel.get_text("label2"))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
