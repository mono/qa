#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class WebControls_WebRadioButton(xsp1TestCase):
    xsp1TestCaseId = 839933
    xsp2TestCaseId = 861815

    def ControlXPath(self, idx):
            return "//*[@id=\"r" + idx + "\"]"

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_radiobutton")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_checked(self.ControlXPath("1")))
            sel.click("r2")
            self.failUnless(sel.is_checked(self.ControlXPath("2")))
            self.failIf(sel.is_checked(self.ControlXPath("1")))
            sel.click("r3")
            self.failUnless(sel.is_checked(self.ControlXPath("3")))
            self.failIf(sel.is_checked(self.ControlXPath("2")))
            self.failIf(sel.is_checked(self.ControlXPath("1")))
            self.failIf(sel.is_checked(self.ControlXPath("4")))
            self.failUnless(sel.is_checked(self.ControlXPath("5")))
            sel.click("r4")
            self.failUnless(sel.is_checked(self.ControlXPath("4")))
            self.failIf(sel.is_checked(self.ControlXPath("5")))
    
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
