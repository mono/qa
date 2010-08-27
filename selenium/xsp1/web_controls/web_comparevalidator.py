#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase


class WebControls_WebCompareValidator(xsp1TestCase):
    xsp1TestCaseId = 838901
    xsp2TestCaseId = 861805
    xsp4TestCaseId = None

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_comparevalidator")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("Enter twice the same string:"))
            sel.type("Text1", "asdfer adf we")
            sel.type("Text2", "asdfer adf we")

            if not mono.usexsp2:
                checkButtonXPath = "_ctl4"
                messageXPath = "//*[@id=\"_ctl3\"]"
            else:
                checkButtonXPath = "ctl04"
                messageXPath = "//*[@id=\"ctl03\"]"

            sel.click(checkButtonXPath)
            sel.wait_for_page_to_load("30000")
            self.failIf(sel.is_visible(messageXPath))
            self.assertEqual("Entered data is valid.", sel.get_text("message"))
            sel.type("Text2", "wrtvasd asdtrqwer")
            sel.click(checkButtonXPath)
            self.failUnless(sel.is_visible(messageXPath))
            sel.type("Text1", "Another test string")
            sel.type("Text2", "Another test string")
            sel.click(checkButtonXPath)
            sel.wait_for_page_to_load("30000")
            self.failIf(sel.is_visible(messageXPath))
            self.assertEqual("Entered data is valid.", sel.get_text("message"))
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
