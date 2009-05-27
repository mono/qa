#!/usr/bin/env python

import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class WebControls_Calendar(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 838895 # xsp1 test case id
        else:
            self.testcaseid = 861728 # xsp2 test case id

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=calendar")
            sel.wait_for_page_to_load("30000")

            if not mono.usexsp2:
                calendarXPath = "//form[@id='_ctl1']/h3"
            else:
                calendarXPath = "//form[@id='ctl01']/h3"

            self.assertEqual("Calendar and properties", sel.get_text(calendarXPath))
            sel.click("link=14")
            sel.wait_for_page_to_load("30000")

            try:
                self.failUnless(sel.is_text_present("14"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

            try:
                self.failUnless(sel.is_text_present("16"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

            sel.click("link=16")
            sel.wait_for_page_to_load("30000")

            try:
                self.failUnless(sel.is_text_present("20"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

            sel.click("link=20")
            sel.wait_for_page_to_load("30000")
        except Exception,e:
            self.verificationErrors.append(str(e))

if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
