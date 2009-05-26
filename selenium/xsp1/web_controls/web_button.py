#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_WebButton(seleniumTestCase):
    testcaseid = 839925

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=web_button")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_element_present("//*[@id=\"btn\"]"))
        sel.click("btn")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_element_present("//*[@id=\"btn\"]"))

if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
