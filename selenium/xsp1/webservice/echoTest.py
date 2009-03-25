#!/usr/bin/env python

import sys
sys.path.append('../..')
from selenium import selenium
from monotesting import *

import unittest, time, re



class echoTest(unittest.TestCase):
    def setUp(self):
        self.testcaseid = 426296
        self.verificationErrors = []
        self.selenium = selenium(rc_server, rc_port, rc_browser, xsp1_url)
        self.selenium.start()
    
    def test_new(self):
        sel = self.selenium
        sel.open("/index.aspx")
        sel.click("link=TestService.asmx")
        sel.wait_for_page_to_load("30000")
        sel.click("link=Echo")
        sel.wait_for_page_to_load("30000")
        sel.click("//a[2]/span")
        sel.wait_for_page_to_load("30000")
        sel.type("a", "this is a test")
        sel.click("//input[@value='Invoke']")
        sel.wait_for_page_to_load("30000")
        try: 
            self.failUnless(re.search(r"^[\s\S]*this is a test[\s\S]*$", sel.get_text("//html/body/table/tbody/tr/td[2]/div/div/div")))
            passTestCase(self.testcaseid)

        except AssertionError, e:
            self.verificationErrors.append(str(e))
            failTestCase(self.testcaseid)
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    monotesting_main()
