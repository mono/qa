#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class WebControls_WebLabel(xsp1TestCase):
    xsp1TestCaseId = 839929
    xsp2TestCaseId = 861818
    Label1Xpath = "//*[@id=\"lbl1\"]"
    Label2XPath = "//*[@id=\"lbl2\"]"
    
    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_label")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_element_present(self.Label1Xpath))
            self.assertEqual("Text as property. This added in Page_Load.", sel.get_text("lbl1"))
            self.failUnless(sel.is_element_present(self.Label2XPath))
            self.assertEqual("Text between tags", sel.get_text("lbl2"))
        
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
