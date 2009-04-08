#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_Temperature(seleniumTestCase):
    testcaseid = 839922
    
    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=temperature")
        sel.wait_for_page_to_load("30000")
        sel.select("//*[@id=\"fromScale\"]", "Celsius")
        sel.type("degrees", "23")
        sel.select("//*[@id=\"toScale\"]", "Farenheit")
        sel.click("//*[@id=\"btn\"]")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_element_present("//*[@id=\"result\"]"))
        self.assertEqual("Converting 23 from Celsius to Farenheit gives 73.4", sel.get_text("result"))
        sel.select("//*[@id=\"fromScale\"]", "Farenheit")
        sel.type("degrees", "23")
        sel.select("//*[@id=\"toScale\"]", "Farenheit")
        sel.click("//*[@id=\"btn\"]")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_element_present("//*[@id=\"result\"]"))
        self.assertEqual("Converting 23 from Farenheit to Farenheit gives 23", sel.get_text("result"))
        sel.select("//*[@id=\"fromScale\"]", "Kelvin")
        sel.type("degrees", "23")
        sel.select("//*[@id=\"toScale\"]", "Farenheit")
        sel.click("//*[@id=\"btn\"]")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_element_present("//*[@id=\"result\"]"))
        self.assertEqual("Converting 23 from Kelvin to Farenheit gives -598", sel.get_text("result"))
        sel.select("//*[@id=\"fromScale\"]", "Kelvin")
        sel.type("degrees", "23")
        sel.select("//*[@id=\"toScale\"]", "Celsius")
        sel.click("//*[@id=\"btn\"]")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_element_present("//*[@id=\"result\"]"))
        self.assertEqual("Converting 23 from Farenheit to Farenheit gives -350", sel.get_text("result"))

if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
