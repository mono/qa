#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_WebTable2(seleniumTestCase):
    testcaseid = 839935

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=web_table2")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_element_present("//html/body/form/table"))
        self.assertEqual("TEST", sel.get_text("//form[@id='_ctl1']/table/tbody/tr/td"))

if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
