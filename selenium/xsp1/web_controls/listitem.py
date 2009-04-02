#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_ListItem(seleniumTestCase):
    testcaseid = 

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=listitem")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_text_present("ListItem test"))
        self.assertEqual("One", sel.get_selected_label("//*[@id=\"NumberList\"]"))
        sel.select("NumberList", "label=Two")
        self.assertEqual("Two", sel.get_selected_label("//*[@id=\"NumberList\"]"))
        sel.select("NumberList", "label=Five")
        self.assertEqual("Five", sel.get_selected_label("//*[@id=\"NumberList\"]"))
        sel.select("NumberList", "label=Eight")
        self.assertEqual("Eight", sel.get_selected_label("//*[@id=\"NumberList\"]"))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
