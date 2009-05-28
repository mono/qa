#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class HtmlControls_HtmlInputText(xsp1TestCase):
    xsp1TestCaseId = 838458
    xsp2TestCaseId = 861717

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=htmlinputtext")
            sel.wait_for_page_to_load("30000")
            sel.type("asText", "My name goes here")
            sel.type("asPassword", "password")
    
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
