#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class AspNetFramework_SerialTest(seleniumTestCase):
    testcaseid = 837578

    def test_new(self):
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=serial")
            sel.wait_for_page_to_load("30000")

            for ix in range(30):
                sel.click("_ctl2")
                sel.wait_for_page_to_load("30000")

                try:
                    self.assertEqual("Old value: " + str(ix), sel.get_text("//html/body/form/span/b"))
                except AssertionError, e:
                    self.verificationErrors.append(str(e))

        except AssertionError, e:
            self.verificationErrors.append(str(e))

if __name__ == "__main__":
    monotesting_main()



# vim:ts=4:expandtab:
