#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class AspNetFramework_TransferTest(seleniumTestCase):
    testcaseid = 837584

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=transfer1")
            sel.wait_for_page_to_load("30000")

            try:
                self.failUnless(sel.is_text_present("FilePath: /1.1/asp.net/transfer1.aspx"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

            try:
                self.failUnless(sel.is_text_present("CurrentExecutionFilePath: /1.1/asp.net/transfer2.aspx"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

        except AssertionError, e: self.verificationErrors.append(str(e))



if __name__ == "__main__":
    monotesting_main()



# vim:ts=4:expandtab:
