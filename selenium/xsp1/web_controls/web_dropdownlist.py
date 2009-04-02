#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_WebDropDownList(seleniumTestCase):
    testcaseid = 

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=web_dropdownlist")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_element_present("//*[@id=\"ddl\"]"))
        self.assertEqual("Item 1", sel.get_selected_label("//*[@id=\"ddl\"]"))
        sel.click("btn")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("You selected 'Item 1' (index #0).", sel.get_text("lbl"))
        sel.select("ddl", "label=Item 4")
        self.assertEqual("Item 4", sel.get_selected_label("//*[@id=\"ddl\"]"))
        sel.click("btn")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("You selected 'Item 4' (index #3).", sel.get_text("lbl"))
        sel.select("ddl", "label=Item 2")
        self.assertEqual("Item 2", sel.get_selected_label("//*[@id=\"ddl\"]"))
        sel.click("btn")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("You selected 'Item 2' (index #1).", sel.get_text("lbl"))
        sel.select("ddl", "label=Item 3")
        self.assertEqual("Item 3", sel.get_selected_label("//*[@id=\"ddl\"]"))
        sel.click("btn")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("You selected 'Item 3' (index #2).", sel.get_text("lbl"))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
