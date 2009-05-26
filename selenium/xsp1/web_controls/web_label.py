#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_WebLabel(seleniumTestCase):
    testcaseid = 839929

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=web_label")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_element_present("//*[@id=\"lbl1\"]"))
        self.assertEqual("Text as property. This added in Page_Load.", sel.get_text("lbl1"))
        self.failUnless(sel.is_element_present("//*[@id=\"lbl2\"]"))
        self.assertEqual("Text between tags", sel.get_text("lbl2"))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
