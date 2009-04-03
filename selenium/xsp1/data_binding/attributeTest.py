#!/usr/bin/env python

import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re


class DataBinding_AttributeTest(seleniumTestCase):
    testcaseid = 839039

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=databind-attribute")
        sel.wait_for_page_to_load("30000")
        sel.select("list", "label=Two")
        sel.wait_for_page_to_load("30000")

        try:
            self.assertEqual("Two", sel.get_text("//*[@id=\"msg\"]"))
        except AssertionError, e:
            self.verificationErrors.append(str(e))

        sel.select("list", "label=One")
        sel.wait_for_page_to_load("30000")

        try:
            self.assertEqual("One", sel.get_text("//*[@id=\"msg\"]"))
        except AssertionError, e:
            self.verificationErrors.append(str(e))

        sel.select("list", "label=Five")
        sel.wait_for_page_to_load("30000")

        try:
            self.assertEqual("Five", sel.get_text("//*[@id=\"msg\"]"))
        except AssertionError, e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    monotesting_main()





# vim:ts=4:expandtab:
