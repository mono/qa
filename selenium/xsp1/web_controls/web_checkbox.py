#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_WebCheckBox(seleniumTestCase):
    testcaseid = 838900

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=web_checkbox")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_element_present("//*[@id=\"chk\"]"))
        self.failIf(sel.is_checked("//*[@id=\"chk\"]"))
        sel.check("//*[@id=\"chk\"]")
        self.failUnless(sel.is_checked("//*[@id=\"chk\"]"))
        self.failUnless(sel.is_element_present("//*[@id=\"chk2\"]"))
        self.failIf(sel.is_checked("//*[@id=\"chk2\"]"))
        sel.check("//*[@id=\"chk2\"]")
        self.failUnless(sel.is_checked("//*[@id=\"chk2\"]"))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
