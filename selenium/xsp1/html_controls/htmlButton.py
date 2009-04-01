#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class HtmlControls_HtmlButton(seleniumTestCase):
    testcaseid = 838536
    
    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=htmlbutton")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_element_present("//*[@id=\"myButton\"]"))
        sel.click("myButton")
        self.failUnless(sel.is_element_present("//*[@id=\"myButton\"]"))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
