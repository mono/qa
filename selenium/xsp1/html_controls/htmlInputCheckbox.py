#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class HtmlControls_HtmlInputCheckbox(seleniumTestCase):
    testcaseid = 838540

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=htmlinputcheckbox")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_element_present("//*[@id=\"myCheckBox\"]"))
        self.failUnless(sel.is_checked("//*[@id=\"myCheckBox\"]"))
        sel.click("myCheckBox")
        self.failIf(sel.is_checked("//*[@id=\"myCheckBox\"]"))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
