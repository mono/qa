#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class Handlers_Async(seleniumTestCase):
    testcaseid = 840261 

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=async.ashx")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("In async callback\nEnd request being invoked.", sel.get_text("//pre"))

if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
