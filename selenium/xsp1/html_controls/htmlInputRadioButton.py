#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class HtmlControls_HtmlInputRadioButton(seleniumTestCase):
    testcaseid = 838544

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=htmlinputradiobutton")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("One\n Two\n Three\n One bis\n Two bis", sel.get_text("_ctl1"))
        self.failUnless(sel.is_checked("//*[@id=\"rb3\"]"))
        sel.click("rb1")
        self.failIf(sel.is_checked("//*[@id=\"rb3\"]"))
        self.failUnless(sel.is_checked("//*[@id=\"rb5\"]"))
        sel.click("rb4")
        self.failIf(sel.is_checked("//*[@id=\"rb5\"]"))

if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
