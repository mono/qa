#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class HtmlControls_HtmlInputFile(seleniumTestCase):
    testcaseid = 838541

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=htmlinputfile")
        sel.wait_for_page_to_load("30000")
        sel.type("myFile", "test.jpg")
        sel.click("smt")
        sel.wait_for_page_to_load("30000")
        try: self.failUnless(sel.is_text_present("Pick a JPEG file"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
