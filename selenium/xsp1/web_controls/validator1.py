#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_Validator1(seleniumTestCase):
    testcaseid = 839923

    def test(self):
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
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
