#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class WebControls_WebLinkButton(xsp1TestCase):
    xsp1TestCaseId = 839930
    xsp2TestCaseId = 861819
    Label1Xpath = "//*[@id=\"lb1\"]"
    Label2XPath = "//*[@id=\"lb2\"]"

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_linkbutton")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_element_present(self.Label1Xpath))
            self.assertEqual("Click me!", sel.get_text("lb1"))
            self.failUnless(sel.is_element_present(self.Label2XPath))
            try: self.assertEqual("Remove this link.", sel.get_text("lb2"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.click("lb2")
            sel.wait_for_page_to_load("30000")
            self.failIf(sel.is_element_present("lb2"))
            self.assertEqual("There used to be a link here, but you have removed it", sel.get_text("label2"))
    
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
