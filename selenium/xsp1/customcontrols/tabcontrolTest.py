#!/usr/bin/env python

import sys
sys.path.append('../..')
from selenium import selenium
from monotesting import *

import unittest, time, re

class tabcontrolTest(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(rc_server, rc_port, rc_browser, xsp1_url)
        self.selenium.start()
    
    def test_new(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=tabcontrol")
        sel.wait_for_page_to_load("30000")
        sel.click("submit")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("Mono Project", sel.get_text("//html/body/form/table[2]/tbody/tr/td[2]/font"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("name", "google")
        sel.type("url", "http://google.com")
        sel.click("submit")
        sel.wait_for_page_to_load("30000")
        try: self.failUnless(sel.is_element_present("//html/body/form/table[2]/tbody/tr/td[4]/a"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
