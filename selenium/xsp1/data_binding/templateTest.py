#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class templateTest(seleniumTestCase):
    testcaseid = 840312 

    def test_new(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=databind-template")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("odd", sel.get_text("//html/body/form/table/tbody/tr[6]/td/b"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("even", sel.get_text("//html/body/form/table/tbody/tr[5]/td/b"))
        except AssertionError, e: self.verificationErrors.append(str(e))

if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
