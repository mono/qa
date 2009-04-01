#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class AspNetFramework_includeTest(seleniumTestCase):
    testcaseid = 838724

    def test(self):
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
        try: self.failUnless(sel.is_text_present("Message text changed2!"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        self.failUnless(sel.is_text_present("Text changed!"))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
