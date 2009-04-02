#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_WebCheckBoxList(seleniumTestCase):
    testcaseid = 

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=web_checkboxlist")
        sel.wait_for_page_to_load("30000")
        self.failIf(sel.is_checked("//*[@id=\"l1_0\"]"))
        sel.click("//*[@id=\"l1_0\"]")
        self.failUnless(sel.is_checked("//*[@id=\"l1_0\"]"))
        self.failIf(sel.is_checked("//*[@id=\"l1_1\"]"))
        sel.click("//*[@id=\"l1_1\"]")
        self.failUnless(sel.is_checked("//*[@id=\"l1_1\"]"))
        self.failIf(sel.is_checked("//*[@id=\"l1_2\"]"))
        sel.click("//*[@id=\"l1_2\"]")
        self.failUnless(sel.is_checked("//*[@id=\"l1_2\"]"))
        self.failIf(sel.is_checked("//*[@id=\"l1_3\"]"))
        sel.click("//*[@id=\"l1_3\"]")
        self.failUnless(sel.is_checked("//*[@id=\"l1_3\"]"))
        self.failIf(sel.is_checked("//*[@id=\"l2_0\"]"))
        sel.click("//*[@id=\"l2_0\"]")
        self.failUnless(sel.is_checked("//*[@id=\"l2_0\"]"))
        self.failIf(sel.is_checked("//*[@id=\"l2_1\"]"))
        sel.click("//*[@id=\"l2_1\"]")
        self.failUnless(sel.is_checked("//*[@id=\"l2_1\"]"))
        self.failIf(sel.is_checked("//*[@id=\"l2_2\"]"))
        sel.click("//*[@id=\"l2_2\"]")
        self.failUnless(sel.is_checked("//*[@id=\"l2_2\"]"))
        self.failIf(sel.is_checked("//*[@id=\"l2_3\"]"))
        sel.click("//*[@id=\"l2_3\"]")
        self.failUnless(sel.is_checked("//*[@id=\"l2_3\"]"))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
