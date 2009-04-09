#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class Hanlders_WebHandler(seleniumTestCase):
    testcaseid = 840264 

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=webhandler.ashx")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Hi there!", sel.get_text("//h1"))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
