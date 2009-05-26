#!/usr/bin/env python

import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class HtmlControls_HtmlGeneric(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 838537
        else:
            self.testcaseid = None

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=htmlgeneric")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("This is ok"))
    
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
