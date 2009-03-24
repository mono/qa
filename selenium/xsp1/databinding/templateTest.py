#!/usr/bin/env python

import sys
sys.path.append('../..')
from selenium import selenium
from monotesting import *

import unittest, time, re

class templateTest(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(rc_server, rc_port, rc_browser, xsp1_url)
        self.selenium.start()
    
    def test_new(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=databind-template")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("odd", sel.get_text("//html/body/form/table/tbody/tr[6]/td/b"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.assertEqual("even", sel.get_text("//html/body/form/table/tbody/tr[5]/td/b"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
