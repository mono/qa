#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase


class WebControls_WebImageButton(xsp1TestCase):
    xsp1TestCaseId = 838904
    xsp2TestCaseId = 863230
    xsp4TestCaseId = None

    def test(self):
        if not self.canRun:
            return
        try:
            imageButtonXPath = "//*[@id=\"imgButton\"]"

            sel = self.selenium
            sel.open("/")
            sel.click("link=web_imagebutton")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_element_present(imageButtonXPath))
            #sel.click("imgButton")
            for ix in range(5):
                sel.click(imageButtonXPath)
                sel.wait_for_page_to_load("30000")
                self.failUnless(sel.is_element_present(imageButtonXPath))
        except Exception,e:
            self.verificationErrors.append(str(e))

if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
