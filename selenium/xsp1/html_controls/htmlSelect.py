#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class HtmlControls_HtmlSelect(seleniumTestCase):
    testcaseid = 838545
    
    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=htmlselect")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_text_present("Select a language:"))
        self.failUnless(sel.is_element_present("//*[@id=\"lselect\"]"))
        self.assertEqual("C", sel.get_selected_label("lselect"))
        sel.select("lselect", "label=C++")
        self.assertEqual("C++", sel.get_selected_label("lselect"))


if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
