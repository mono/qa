#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_Dbpage1(seleniumTestCase):
    testcaseid = 838897

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=dbpage1")
        sel.wait_for_page_to_load("30000")
        sel.type("PersonFilter", "%shrek%")
        sel.click("btn")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Shrek Ogre", sel.get_text("//table[@id='myTable']/tbody/tr/td[1]"))
        self.assertEqual("shrek@farfaraway.com", sel.get_text("//table[@id='myTable']/tbody/tr/td[2]"))
        sel.type("PersonFilter", "%")
        sel.type("MailFilter", "%duck%")
        sel.click("btn")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Donald Duck", sel.get_text("//table[@id='myTable']/tbody/tr/td[1]"))
        self.assertEqual("donald.duck@donaldinho.com", sel.get_text("//table[@id='myTable']/tbody/tr/td[2]"))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
