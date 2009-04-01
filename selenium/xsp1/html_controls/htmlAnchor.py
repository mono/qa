#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class HtmlControls_HtmlAnchor(seleniumTestCase):
    testcaseid = 838535

    def test_new(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=htmlanchor")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_text_present("Go mono!"))
        sel.click("myAnchor")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_text_present("Mono Project News"))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
