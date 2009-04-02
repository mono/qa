#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_WebXML(seleniumTestCase):
   testcaseid = 838910
    
    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=web_xml")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Xml Example", sel.get_text("//h3"))
        self.assertEqual("Joe   Suits", sel.get_text("//form[@id='_ctl1']/table[1]/tbody/tr[1]/td/b"))
        self.assertEqual("Job Title: CEO\n Description: Wears the nice suit", sel.get_text("//form[@id='_ctl1']/table[1]/tbody/tr[3]/td"))
        self.assertEqual("Jeremy   Boards", sel.get_text("//form[@id='_ctl1']/table[3]/tbody/tr[1]/td/b"))
        self.assertEqual("Job Title: Pro Surfer\n Description: Rides the big waves", sel.get_text("//form[@id='_ctl1']/table[3]/tbody/tr[3]/td"))
        self.assertEqual("Joan   Page", sel.get_text("//form[@id='_ctl1']/table[4]/tbody/tr[1]/td/b"))
        self.assertEqual("Job Title: Web Site Developer\n Description: Writes the pretty pages", sel.get_text("//form[@id='_ctl1']/table[4]/tbody/tr[3]/td"))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
