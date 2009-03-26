#!/usr/bin/env python

import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re


class echoTest(seleniumTestCase):
    testcaseid = 426296

    def test_new(self):
        print "derived class.test()"
        if not self.canRun:
            return
        try: 
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
            self.failUnless(re.search(r"^[\s\S]*this is a test[\s\S]*$", sel.get_text("//html/body/table/tbody/tr/td[2]/div/div/div")))

        except Exception, e:
            print "test_new() except"
            self.verificationErrors.append(str(e))
    

if __name__ == "__main__":
    monotesting_main()
