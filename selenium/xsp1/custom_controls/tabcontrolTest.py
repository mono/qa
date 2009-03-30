#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class AspNetFramework_RegisterTest(seleniumTestCase):
    testcaseid = 837902

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=tabcontrol")
        sel.wait_for_page_to_load("30000")
        sel.click("submit")
        sel.wait_for_page_to_load("30000")
        sel.type("name", "Google")

        try:
            self.assertEqual("Mono Project", sel.get_table("//form[@id='_ctl1']/table[2].0.1"))
        except AssertionError, e:
            self.verificationErrors.append(str(e))

        sel.type("url", "http://google.com")
        sel.click("submit")
        sel.wait_for_page_to_load("30000")

        try:
            self.assertEqual("Google", sel.get_table("//form[@id='_ctl1']/table[2].0.3"))
        except AssertionError, e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    monotesting_main()



# vim:ts=4:expandtab:
