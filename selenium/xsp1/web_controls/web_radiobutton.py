#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_WebRadioButton(seleniumTestCase):
    testcaseid = 839933

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=web_radiobutton")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_checked("//*[@id=\"r1\"]"))
        sel.click("r2")
        self.failUnless(sel.is_checked("//*[@id=\"r2\"]"))
        self.failIf(sel.is_checked("//*[@id=\"r1\"]"))
        sel.click("r3")
        self.failUnless(sel.is_checked("//*[@id=\"r3\"]"))
        self.failIf(sel.is_checked("//*[@id=\"r2\"]"))
        self.failIf(sel.is_checked("//*[@id=\"r1\"]"))
        self.failIf(sel.is_checked("//*[@id=\"r4\"]"))
        self.failUnless(sel.is_checked("//*[@id=\"r5\"]"))
        sel.click("r4")
        self.failUnless(sel.is_checked("//*[@id=\"r4\"]"))
        self.failIf(sel.is_checked("//*[@id=\"r5\"]"))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
