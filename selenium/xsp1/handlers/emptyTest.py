#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class Handlers_Empty(xsp1TestCase):
    xsp1TestCaseId = 840263
    xsp2TestCaseId = 861699

    def test(self):
        BodyXpath = "//html"
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=empty.ashx")
            try: self.failUnless(sel.is_element_present(BodyXpath))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present(BodyXpath))
            except AssertionError, e: self.verificationErrors.append(str(e))

        except Exception,e:
            self.verificationErrors.append(str(e))

if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
