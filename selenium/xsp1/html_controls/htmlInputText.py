#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class HtmlControls_HtmlInputText(seleniumTestCase):
    testcaseid = 838458

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=htmlinputtext")
        sel.wait_for_page_to_load("30000")
        sel.type("asText", "My name goes here")
        sel.type("asPassword", "password")
    

if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
