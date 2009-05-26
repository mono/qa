#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_WebTextBox(seleniumTestCase):
    testcaseid = 839936
    
    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=web_textbox")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_element_present("//*[@id=\"txt1\"]"))
        sel.type("txt1", "This is \nmultiline text")
        self.failUnless(sel.is_element_present("//*[@id=\"txt2\"]"))
        sel.type("txt2", "This is a single line")
        self.failUnless(sel.is_element_present("//*[@id=\"txt3\"]"))
        sel.type("txt3", "password")
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
