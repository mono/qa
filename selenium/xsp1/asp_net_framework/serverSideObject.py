#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class AspNetFramework_serverSideObject(seleniumTestCase):
    testcaseid = 838725

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=server-side-object")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Here is a value: One", sel.get_text("//table[@id='MyList']/tbody/tr[1]/td"))
        self.assertEqual("Here is a value: Two", sel.get_text("//table[@id='MyList']/tbody/tr[2]/td"))
        self.assertEqual("Here is a value: Three", sel.get_text("//table[@id='MyList']/tbody/tr[3]/td"))

if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
