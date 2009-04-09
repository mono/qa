#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class Handlers_Empty(seleniumTestCase):
    testcaseid = 840263 

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=empty.ashx")
        try: self.failUnless(sel.is_element_present("//html"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("//body"))
        except AssertionError, e: self.verificationErrors.append(str(e))

if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
