#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class Handlers_Async(xsp1TestCase):
    xsp1TestCaseId = 840261
    xsp2TestCaseId = 861696
    xsp4TestCaseId = None
    
    def test(self):
        TestElementXpath = "//pre"
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=async.ashx")
            sel.wait_for_page_to_load("30000")
            self.assertEqual("In async callback\nEnd request being invoked.", sel.get_text(TestElementXpath))

        except Exception,e:
            self.verificationErrors.append(str(e))

if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
