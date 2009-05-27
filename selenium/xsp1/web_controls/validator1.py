#!/usr/bin/env python

import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class WebControls_Validator1(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 839923 # xsp1 test case id
        else:
            self.testcaseid = 861797 # xsp2 test case id

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=validator1")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_element_present("//*[@id=\"txt1\"]"))
            self.failIf(sel.is_visible("//*[@id=\"validTxt1\"]"))
            self.failIf(sel.is_visible("//*[@id=\"validtxt2\"]"))
            self.failIf(sel.is_visible("//*[@id=\"validtxt3\"]"))
            sel.type("txt1", "This is \nmultiline text\n\nTest test test.")
            sel.type("txt2", "single line")
            sel.type("txt3", "password")
            sel.click("btn")
            sel.wait_for_page_to_load("30000")
            self.failIf(sel.is_visible("//*[@id=\"validTxt1\"]"))
            self.failIf(sel.is_visible("//*[@id=\"validtxt2\"]"))
            self.failIf(sel.is_visible("//*[@id=\"validtxt3\"]"))
            sel.type("txt1", "")
            sel.type("txt2", "single line")
            sel.type("txt3", "password")
            sel.click("btn")
            self.failUnless(sel.is_visible("//*[@id=\"validTxt1\"]"))
            self.failIf(sel.is_visible("//*[@id=\"validtxt2\"]"))
            self.failIf(sel.is_visible("//*[@id=\"validtxt3\"]"))
            sel.type("txt1", "This is \nmultiline text\n\nTest test test.")
            sel.type("txt2", "")
            sel.type("txt3", "password")
            sel.click("btn")
            self.failIf(sel.is_visible("//*[@id=\"validTxt1\"]"))
            self.failUnless(sel.is_visible("//*[@id=\"validtxt2\"]"))
            self.failIf(sel.is_visible("//*[@id=\"validtxt3\"]"))
            sel.type("txt1", "This is \nmultiline text\n\nTest test test.")
            sel.type("txt2", "single line")
            sel.type("txt3", "")
            sel.click("btn")
            self.failIf(sel.is_visible("//*[@id=\"validTxt1\"]"))
            self.failIf(sel.is_visible("//*[@id=\"validtxt2\"]"))
            self.failUnless(sel.is_visible("//*[@id=\"validtxt3\"]"))
            sel.type("txt1", "")
            sel.type("txt2", "")
            sel.type("txt3", "")
            sel.click("btn")
            self.failUnless(sel.is_visible("//*[@id=\"validTxt1\"]"))
            self.failUnless(sel.is_visible("//*[@id=\"validtxt2\"]"))
            self.failUnless(sel.is_visible("//*[@id=\"validtxt3\"]"))
            sel.type("txt1", "This is \nmultiline text\n\nTest test test.")
            sel.type("txt2", "single line")
            sel.type("txt3", "password")
            sel.click("btn")
            sel.wait_for_page_to_load("30000")
            self.failIf(sel.is_visible("//*[@id=\"validTxt1\"]"))
            self.failIf(sel.is_visible("//*[@id=\"validtxt2\"]"))
            self.failIf(sel.is_visible("//*[@id=\"validtxt3\"]"))
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
