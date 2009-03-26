#!/usr/bin/env python

import sys
sys.path.append('../..')
from selenium import selenium
from monotesting import *

import unittest, time, re

class loginTest(unittest.TestCase):
    def setUp(self):
        self.testcaseid=426290
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
        sel.click("//html/body/form/input[2]")
        sel.wait_for_page_to_load("30000")
        sel.click("link=Authentication")
        sel.wait_for_page_to_load("30000")
        try:
            self.assertEqual("Signout", sel.get_value("//html/body/form/input"))
            passTestCase(self.testcaseid)

        except AssertionError, e:
            self.verificationErrors.append(str(e))
            failTestCase(self.testcaseid)
    
    def tearDown(self):
        self.selenium.stop()
        updateTestCase(self.testcaseid,len(self.verificationErrors) == 0)
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    monotesting_main()