#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_WebPlaceHolder(seleniumTestCase):
    testcaseid = 839932

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=web_placeholder")
        sel.wait_for_page_to_load("30000")
        self.failIf(sel.is_checked("//*[@id=\"_ctl2\"]"))
        sel.click("_ctl2")
        self.failUnless(sel.is_checked("//*[@id=\"_ctl2\"]"))
        sel.click("link=Mono project Home Page")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Main Page - Mono", sel.get_title())

if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
