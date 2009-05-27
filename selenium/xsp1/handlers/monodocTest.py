#!/usr/bin/env python

import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class Handlers_MonoDoc(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 840265
        else:
            self.testcaseid = 861700 

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
