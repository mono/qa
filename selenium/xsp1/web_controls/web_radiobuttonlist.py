#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_WebRadioButtonList(seleniumTestCase):
    testcaseid = 

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=web_radiobuttonlist")
        sel.wait_for_page_to_load("30000")
        self.failIf(sel.is_checked("//*[@id=\"rbl1_0\"]"))
        sel.click("rbl1_0")
        self.failUnless(sel.is_checked("//*[@id=\"rbl1_0\"]"))
        self.failIf(sel.is_checked("//*[@id=\"rbl1_1\"]"))
        sel.click("rbl1_1")
        self.failUnless(sel.is_checked("//*[@id=\"rbl1_1\"]"))
        self.failIf(sel.is_checked("//*[@id=\"rbl1_0\"]"))
        self.failIf(sel.is_checked("//*[@id=\"rbl1_2\"]"))
        sel.click("rbl1_2")
        self.failUnless(sel.is_checked("//*[@id=\"rbl1_2\"]"))
        self.failIf(sel.is_checked("//*[@id=\"rbl1_3\"]"))
        self.failIf(sel.is_checked("//*[@id=\"rbl1_3\"]"))
        sel.click("rbl1_3")
        self.failUnless(sel.is_checked("//*[@id=\"rbl1_3\"]"))
        self.failIf(sel.is_checked("//*[@id=\"rbl1_2\"]"))
        self.failIf(sel.is_checked("//*[@id=\"rbl1_5\"]"))
        sel.click("rbl1_5")
        self.failUnless(sel.is_checked("//*[@id=\"rbl1_5\"]"))
        self.failIf(sel.is_checked("//*[@id=\"rbl1_3\"]"))
        self.failIf(sel.is_checked("//*[@id=\"rbl2_0\"]"))
        sel.click("rbl2_0")
        self.failUnless(sel.is_checked("//*[@id=\"rbl2_0\"]"))
        self.failIf(sel.is_checked("//*[@id=\"rbl2_1\"]"))
        sel.click("rbl2_1")
        self.failUnless(sel.is_checked("//*[@id=\"rbl2_1\"]"))
        self.failIf(sel.is_checked("//*[@id=\"rbl2_0\"]"))
        self.failIf(sel.is_checked("//*[@id=\"rbl2_2\"]"))
        sel.click("rbl2_2")
        self.failUnless(sel.is_checked("//*[@id=\"rbl2_2\"]"))
        self.failIf(sel.is_checked("//*[@id=\"rbl2_3\"]"))
        self.failIf(sel.is_checked("//*[@id=\"rbl2_3\"]"))
        sel.click("rbl2_3")
        self.failUnless(sel.is_checked("//*[@id=\"rbl2_3\"]"))
        self.failIf(sel.is_checked("//*[@id=\"rbl2_2\"]"))
        self.failIf(sel.is_checked("//*[@id=\"rbl2_5\"]"))
        sel.click("rbl2_5")
        self.failUnless(sel.is_checked("//*[@id=\"rbl2_5\"]"))
        self.failIf(sel.is_checked("//*[@id=\"rbl2_3\"]"))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
