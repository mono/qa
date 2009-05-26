#!/usr/bin/env python

import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class HtmlControls_Button(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 838534
        else:
            self.testcaseid = None

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=button")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("HtmlButton Sample"))
            sel.click("Button1")
            self.assertEqual("You activated Button1", sel.get_text("Span1"))
            self.failUnless(sel.is_element_present("//*[@id=\"Button1\"]"))
            sel.click("Button1")
            sel.wait_for_page_to_load("30000")
            self.assertEqual("You deactivated Button1", sel.get_text("Span1"))
    
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
