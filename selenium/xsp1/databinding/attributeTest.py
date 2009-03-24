#!/usr/bin/env python

import sys
sys.path.append('../..')
from selenium import selenium
from monotesting import *

import unittest, time, re

class attributeTest(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(rc_server, rc_port, rc_browser, xsp1_url)
        self.selenium.start()
    
    def test_new(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=databind-attribute")
        sel.wait_for_page_to_load("30000")
        sel.select("list", "label=Two")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("Two", sel.get_text("//*[@id=\"msg\"]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.select("list", "label=One")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("One", sel.get_text("//*[@id=\"msg\"]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.select("list", "label=Five")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("Five", sel.get_text("//*[@id=\"msg\"]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
