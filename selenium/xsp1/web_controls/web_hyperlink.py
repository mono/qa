#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_WebHyperLink(seleniumTestCase):
    testcaseid = 839927

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=web_hyperlink")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_element_present("//html/body/a/img"))
        sel.click("//img[@alt='Ximian']")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Linux OS | SUSE Linux Enterprise", sel.get_title())

if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
