#!/usr/bin/env python

import sys
sys.path.append('../..')
from selenium import selenium
from monotesting import *

import unittest, time, re

class asyncTest(unittest.TestCase):
    def setUp(self):
        self.testcaseid = None
        self.verificationErrors = []
        self.selenium = selenium(rc_server, rc_port, rc_browser, xsp1_url)
        self.selenium.start()
    
    def test_new(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=async.ashx")
        sel.wait_for_page_to_load("30000")
        try: 
            self.failUnless(sel.is_text_present("End request being invoked."))
            passTestCase(self.testcaseid)
        except AssertionError, e: 
            failTestCase(self.testcaseid)
            self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    monotesting_main()
