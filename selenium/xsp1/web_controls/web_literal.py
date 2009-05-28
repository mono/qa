#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class WebControls_WebLiteral(xsp1TestCase):
    xsp1TestCaseId = 838906
    xsp2TestCaseId = 861821

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_literal")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("Hi there!"))
    
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
