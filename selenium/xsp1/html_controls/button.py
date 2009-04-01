#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class HtmlControls_Button(seleniumTestCase):
    testcaseid = 838534

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=button")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_text_present("HtmlButton Sample"))
        sel.click("Button1")
        self.failUnless(sel.is_element_present("//*[@id=\"Button1\"]"))
        sel.click("Button1")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("You activated Button1", sel.get_text("Span1"))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
