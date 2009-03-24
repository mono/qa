#!/usr/bin/env python

import sys
sys.path.append('../..')
from selenium import selenium
from monotesting import *

import unittest, time, re

class loginTest(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(rc_server, rc_port, rc_browser, xsp1_url)
        self.selenium.start()
    
    def test_new(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=login")
        sel.wait_for_page_to_load("30000")
        sel.type("UserEmail", "jdoe@somewhere.com")
        sel.type("UserPass", "password")
        sel.click("ctl04")
        sel.wait_for_page_to_load("30000")
        sel.click("link=Authentication")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("Signout", sel.get_value("//html/body/form/input"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
