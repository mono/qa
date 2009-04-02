#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class WebControls_WebDataGrid(seleniumTestCase):
    testcaseid = 

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=web_datagrid")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("DataGrid sample", sel.get_text("//h3"))
        self.assertEqual("Country", sel.get_text("//table[@id='dg']/tbody/tr[1]/td[1]"))
        self.assertEqual("Continent", sel.get_text("//table[@id='dg']/tbody/tr[1]/td[2]"))
        self.assertEqual("Abbr", sel.get_text("//table[@id='dg']/tbody/tr[1]/td[3]"))
        self.assertEqual("Spain", sel.get_text("//table[@id='dg']/tbody/tr[2]/td[1]"))
        self.assertEqual("Europe", sel.get_text("//table[@id='dg']/tbody/tr[2]/td[2]"))
        self.assertEqual("es", sel.get_text("//table[@id='dg']/tbody/tr[2]/td[3]"))
        self.assertEqual("Japan", sel.get_text("//table[@id='dg']/tbody/tr[3]/td[1]"))
        self.assertEqual("Asia", sel.get_text("//table[@id='dg']/tbody/tr[3]/td[2]"))
        self.assertEqual("jp", sel.get_text("//table[@id='dg']/tbody/tr[3]/td[3]"))
        self.assertEqual("Mexico", sel.get_text("//table[@id='dg']/tbody/tr[4]/td[1]"))
        self.assertEqual("America", sel.get_text("//table[@id='dg']/tbody/tr[4]/td[2]"))
        self.assertEqual("mx", sel.get_text("//table[@id='dg']/tbody/tr[4]/td[3]"))
    
if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
