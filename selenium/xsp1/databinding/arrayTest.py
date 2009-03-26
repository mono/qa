#!/usr/bin/env python

import sys
sys.path.append('../..')
from selenium import selenium
from monotesting import *

import unittest, time, re

class arrayTest(unittest.TestCase):
    def setUp(self):
        self.testcaseid = None
        self.verificationErrors = []
        self.selenium = selenium(rc_server, rc_port, rc_browser, xsp1_url)
        self.selenium.start()
    
    def test_new(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=databind-arraylist")
        sel.wait_for_page_to_load("30000")
        sel.select("list", "label=Two")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("Selected option: Two", sel.get_text("//*[@id=\"msg\"]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.select("list", "label=Four")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("Selected option: Four", sel.get_text("//*[@id=\"msg\"]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.select("list", "label=One")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("Selected option: One", sel.get_text("//*[@id=\"msg\"]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        updateTestCase(self.testcaseid,len(self.verificationErrors) == 0)
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    monotesting_main()
