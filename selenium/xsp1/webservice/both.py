#!/usr/bin/env python

import sys
import unittest, time, re

sys.path.append('../..')
from selenium import selenium
from monotesting import *


class webservice_tests(unittest.TestCase):

    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(rc_server, rc_port, rc_browser, rc_host)
        self.selenium.start()

    def test_add(self):
        sel = self.selenium
        sel.open("/index.aspx")
        sel.click("link=TestService.asmx")
        sel.wait_for_page_to_load("30000")
        sel.click("link=Add")
        sel.wait_for_page_to_load("30000")
        sel.click("//a[2]/span")
        sel.wait_for_page_to_load("30000")
        sel.type("a", "5238")
        sel.type("b", "8361")
        sel.click("//input[@value='Invoke']")
        sel.wait_for_page_to_load("30000")
        try: self.failUnless(re.search(r"^[\s\S]*13599[\s\S]*$", sel.get_text("//html/body/table/tbody/tr/td[2]/div/div/div")))
        except AssertionError, e: self.verificationErrors.append(str(e))

        self.assertEqual(1,4,"1 should equal 4")

    def test_echo(self):
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
        try: self.failUnless(re.search(r"^[\s\S]*this is a test[\s\S]*$", sel.get_text("//html/body/table/tbody/tr/td[2]/div/div/div")))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
     unittest.main()
