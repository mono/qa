#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class Handlers_MonoDoc (xsp1TestCase):
    xsp1TestCaseId = 840265
    xsp2TestCaseId = 861700

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=monodoc.ashx")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Base Class Library")
            sel.wait_for_page_to_load("30000")
            sel.select_window("name=content")
            sel.click("link=System.Collections")
            sel.wait_for_page_to_load("30000")
            try:
                self.failUnless(sel.is_text_present("System"))
                passTestCase(self.testcaseid)
            except AssertionError, e:
                self.verificationErrors.append(str(e))
                failTestCase(self.testcaseid)
        except Exception,e:
            self.verificationErrors.append(str(e))
            
if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
