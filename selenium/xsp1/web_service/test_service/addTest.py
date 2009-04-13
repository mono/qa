#!/usr/bin/env python

import sys
sys.path.append('../../../..')
from selenium.selenium import selenium
#from selenium.seleniumTestCase import *
from selenium.xsp1 import xsp1TestCase

from common.monotesting import *

import unittest, time, re


class WebService_TestService_AddTest(xsp1TestCase.xsp1TestCase):
    def __init__(self):
     
        if monotesting.is_xsp1:
            self.testcaseid = 837262
            #self.url = base_url + xsp1_port
        else:
            self.testcaseid = 111111 # xsp2 test case id
            #self.url = base_url + xsp2_port

    def test_add(self):
        if not self.canRun:
            return
        try:
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
            self.failUnless(re.search(r"^[\s\S]*13599[\s\S]*$", sel.get_text("//html/body/table/tbody/tr/td[2]/div/div/div")))

        except AssertionError, e:
            self.verificationErrors.append(str(e))



if __name__ == "__main__":
    monotesting_main()





# vim:ts=4:expandtab:
