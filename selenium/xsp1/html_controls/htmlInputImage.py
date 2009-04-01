#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class HtmlControls_HtmlInputImage(seleniumTestCase):
    testcaseid = 838543 

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=htmlinputimage")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_element_present("//*[@id=\"myImageAgain\"]"))
        sel.click("myImageAgain")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_element_present("//*[@id=\"myImageAgain\"]"))

if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
