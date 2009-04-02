#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_DataList(seleniumTestCase):
    testcaseid = 838896

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=datalist")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("Datalist sample", sel.get_text("//h3"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        self.assertEqual("Spain", sel.get_text("//table[@id='dl']/tbody/tr/td[1]/span"))
        self.assertEqual("Japan", sel.get_text("//table[@id='dl']/tbody/tr/td[2]/span"))
        self.assertEqual("Mexico", sel.get_text("//table[@id='dl']/tbody/tr/td[3]/span"))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
