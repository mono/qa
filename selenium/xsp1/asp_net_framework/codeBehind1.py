#!/usr/bin/env python


import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class AspNetFramework_codeBehind1(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 838721 # xsp1 test case id
        else:
            self.testcaseid = 861574 # xsp2 test case id

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=codebehind1")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("Page Loaded"))
            sel.type("TextBox1", "This is some text")
            sel.click("SubmitButton")
            sel.wait_for_page_to_load("30000")
            try:
                self.failUnless(sel.is_text_present("This is some text"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

        except Exception,e:
            self.verificationErrors.append(str(e))

if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
