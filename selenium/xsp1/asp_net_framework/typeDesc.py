#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class AspNetFramework_typeDesc(seleniumTestCase):
    testcaseid = 838728

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=typedesc")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_text_present("Passed!"))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
