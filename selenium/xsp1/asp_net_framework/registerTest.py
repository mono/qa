#!/usr/bin/env python

import sys
sys.path.append('../..')
from selenium import selenium
from monotesting import *

import unittest, time, re

class registerTest(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(rc_server, rc_port, rc_browser, xsp1_url)
        self.selenium.start()
    
    def test_new(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=registertest")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("This is a default Two!", sel.get_text("//*[@id=\"Message2\"]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("_ctl2")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("Message text changed2!", sel.get_text("//*[@id=\"Message2\"]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    monotesting_main()
