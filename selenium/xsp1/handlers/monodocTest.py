#!/usr/bin/env python

import sys
sys.path.append('../..')
from selenium import selenium
from monotesting import *

import unittest, time, re

class monodocTest(unittest.TestCase):
    def setUp(self):
        self.testcaseid = None
        self.verificationErrors = []
        self.selenium = selenium(rc_server, rc_port, rc_browser, xsp1_url)
        self.selenium.start()
    
    def test_new(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=monodoc.ashx")
        sel.wait_for_page_to_load("30000")
        sel.click("link=Base Class Library")
        sel.wait_for_page_to_load("30000")
        sel.select_window("name=content")
        sel.click("link=System.Collections")
        sel.wait_for_page_to_load("30000")
        try:
            self.failUnless(sel.is_text_present("System"))
            passTestCase(self.testcaseid)
        except AssertionError, e:
            self.verificationErrors.append(str(e))
            failTestCase(self.testcaseid)
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    monotesting_main()
