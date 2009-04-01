#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class HtmlControls_HtmlTable(seleniumTestCase):
    testcaseid = 838546

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=htmltable")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Row 0, cell 0", sel.get_text("//table[@id='myTable']/tbody/tr[1]/td[1]"))
        self.assertEqual("Row 4, cell 3", sel.get_text("//table[@id='myTable']/tbody/tr[5]/td[4]"))

if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
