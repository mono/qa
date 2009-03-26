#!/usr/bin/env python

import sys
sys.path.append('../..')
from selenium import selenium
from monotesting import *

import unittest, time, re

class emptyTest(unittest.TestCase):
    def setUp(self):
        self.testcaseid = None
        self.verificationErrors = []
        self.selenium = selenium(rc_server, rc_port, rc_browser, xsp1_url)
        self.selenium.start()
    
    def test_new(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=empty.ashx")
        try:
            self.failUnless(sel.is_text_present(""))
            passTestCase(self.testcaseid)
        except AssertionError, e:
            self.verificationErrors.append(str(e))
            failTestCase(self.testcaseid)
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    monotesting_main()
