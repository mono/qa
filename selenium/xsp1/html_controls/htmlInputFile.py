#!/usr/bin/env python

import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class HtmlControls_HtmlInputFile(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 838541
        else:
            self.testcaseid = None

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=htmlinputfile")
            sel.wait_for_page_to_load("30000")
            sel.type("myFile", "test.jpg")
            sel.click("smt")
            sel.wait_for_page_to_load("30000")
            try: self.failUnless(sel.is_text_present("Pick a JPEG file"))
            except AssertionError, e: self.verificationErrors.append(str(e))
    
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
