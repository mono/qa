#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class Handlers_MonoDoc(seleniumTestCase):
    testcaseid = 840265 

    def test(self):
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

if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
