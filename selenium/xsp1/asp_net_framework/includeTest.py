#!/usr/bin/env python


import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class AspNetFramework_includeTest(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 838724 # xsp1 test case id
        else:
            self.testcaseid = 861577 # xsp2 test case id

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=includetest")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("This is a default One!"))
            self.assertEqual("This is a default Two!", sel.get_text("Message2"))
            self.assertEqual("This is a label!", sel.get_text("Three"))
            sel.click("_ctl2")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("Message text changed!"))
            try:
                self.failUnless(sel.is_text_present("Message text changed2!"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))
            self.failUnless(sel.is_text_present("Text changed!"))

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
