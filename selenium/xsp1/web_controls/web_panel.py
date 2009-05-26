#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_WebPanel(seleniumTestCase):
    testcaseid = 839931

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=web_panel")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Mono site", sel.get_text("hyper"))
        sel.click("hyper")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Main Page - Mono", sel.get_title())
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
