#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_WebRotator(seleniumTestCase):
    testcaseid = 839924

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=web_adrotator")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_element_present("//img[@alt='Mono']"))
        sel.click("//img[@alt='Mono']")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Main Page - Mono", sel.get_title())

if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
