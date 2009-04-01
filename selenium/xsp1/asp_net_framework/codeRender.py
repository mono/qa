#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class AspNetFramework_codeRender(seleniumTestCase):
    testcaseid = 838722

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=code-render")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_text_present("hi! message number 0."))
        self.failUnless(sel.is_text_present("hello message number 1."))
        self.failUnless(sel.is_text_present("hola message number 2."))
        self.failUnless(sel.is_text_present("Ciao message number 3."))
        self.failUnless(sel.is_text_present("adios message number 4."))
        sel.click("link=14")
        sel.wait_for_page_to_load("30000")
        sel.click("link=16")
        sel.wait_for_page_to_load("30000")
        sel.click("link=>")
        sel.wait_for_page_to_load("30000")
        sel.click("link=<")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_text_present("This should say hello: hello"))

if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
