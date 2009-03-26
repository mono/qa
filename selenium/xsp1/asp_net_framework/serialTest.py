#!/usr/bin/env python

import sys
sys.path.append('../..')
from selenium import selenium
from monotesting import *

import unittest, time, re

class serialTest(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(rc_server, rc_port, rc_browser, xsp1_url)
        self.selenium.start()
    
    def test_new(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=serial")
        sel.wait_for_page_to_load("30000")
        sel.click("//html/body/form/input[2]")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("Old value: 0", sel.get_text("//html/body/form/span/b"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//html/body/form/input[2]")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("Old value: 1", sel.get_text("//html/body/form/span/b"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//html/body/form/input[2]")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("Old value: 2", sel.get_text("//html/body/form/span/b"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    monotesting_main()
