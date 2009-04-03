#!/usr/bin/env python

import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re


class DataBinding_arrayTest(seleniumTestCase):
    testcaseid = 839038

    def test_new(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=databind-arraylist")
        sel.wait_for_page_to_load("30000")
        sel.select("list", "label=Two")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("Selected option: Two", sel.get_text("//*[@id=\"msg\"]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.select("list", "label=Four")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("Selected option: Four", sel.get_text("//*[@id=\"msg\"]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.select("list", "label=One")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("Selected option: One", sel.get_text("//*[@id=\"msg\"]"))
        except AssertionError, e: self.verificationErrors.append(str(e))



if __name__ == "__main__":
    monotesting_main()





# vim:ts=4:expandtab:
