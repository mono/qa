#!/usr/bin/env python

import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase
import unittest, time, re

class WebControls_WebPanel(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 839931
        else:
            self.testcaseid = 861812

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_panel")
            sel.wait_for_page_to_load("30000")
            self.assertEqual("Mono site", sel.get_text("hyper"))
            sel.click("hyper")
            sel.wait_for_page_to_load("30000")
            self.assertEqual("Main Page - Mono", sel.get_title())
    
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
