#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class WebControls_WebTextBox(xsp1TestCase):
    xsp1TestCaseId = 839936
    xsp2TestCaseId = 861810
    Element1XPath = "//*[@id=\"txt1\"]"
    Element2XPath = "//*[@id=\"txt2\"]"
    Element3XPath = "//*[@id=\"txt3\"]"
    
    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_textbox")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_element_present(self.Element1XPath))
            sel.type("txt1", "This is \nmultiline text")
            self.failUnless(sel.is_element_present(self.Element2XPath))
            sel.type("txt2", "This is a single line")
            self.failUnless(sel.is_element_present(self.Element3XPath))
            sel.type("txt3", "password")

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
