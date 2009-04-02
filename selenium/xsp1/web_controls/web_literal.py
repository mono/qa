#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_WebLiteral(seleniumTestCase):
    testcaseid =

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=web_literal")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_text_present("Hi there!"))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
