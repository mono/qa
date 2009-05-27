#!/usr/bin/env python

import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class Handlers_Empty(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 840263
        else:
            self.testcaseid = 861699 

    def test(self):
        if not self.canRun:
            return
        try:

            sel = self.selenium
            sel.open("/")
            sel.click("link=empty.ashx")
            try: self.failUnless(sel.is_element_present("//html"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("//body"))
            except AssertionError, e: self.verificationErrors.append(str(e))

        except Exception,e:
            self.verificationErrors.append(str(e))

if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
