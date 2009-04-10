#!/usr/bin/env python
import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *
import unittest, time, re

class CustomControls_tabcontrolTest(seleniumTestCase):
    testcaseid = 840314

    def test(self):
        if not self.canRun:
            return
        sel = self.selenium
        sel.open("/")
        sel.click("link=tabcontrol2")
        sel.wait_for_page_to_load("30000")
        sel.click("link=Image")
        sel.wait_for_page_to_load("30000")
        try: self.failUnless(sel.is_element_present("//*[@id=\"tabs_im\"]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=Form")
        sel.wait_for_page_to_load("30000")
        sel.type("tabs_txt1", "You can write here. ahello")
        sel.click("tabs_btn")
        sel.wait_for_page_to_load("30000")
        try: self.failUnless(re.search(r"^[\s\S]*pressed me 1 time[\s\S]*$", sel.get_text("//*[@id=\"tabs_uno\"]")))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("tabs_btn")
        sel.wait_for_page_to_load("30000")
        try: self.failUnless(re.search(r"^[\s\S]*pressed me 2 times[\s\S]*$", sel.get_text("//*[@id=\"tabs_uno\"]")))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("tabs_txt1", "You can write here. ahellos")
        sel.click("tabs_btn")
        sel.wait_for_page_to_load("30000")
        try: self.failUnless(re.search(r"^[\s\S]*pressed me 3 times[\s\S]*$", sel.get_text("//*[@id=\"tabs_uno\"]")))
        except AssertionError, e: self.verificationErrors.append(str(e))

if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
