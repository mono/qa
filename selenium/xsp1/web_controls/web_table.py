#!/usr/bin/env python


import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase
import unittest, time, re

class WebControls_WebTable(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 838909
        else:
            self.testcaseid = None

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_table")
            sel.wait_for_page_to_load("30000")
            self.assertEqual("Row 0, cell 0", sel.get_text("//table[@id='myTable']/tbody/tr[1]/td[1]"))
            self.assertEqual("Row 0, cell 1", sel.get_text("//table[@id='myTable']/tbody/tr[1]/td[2]"))
            self.assertEqual("Row 0, cell 2", sel.get_text("//table[@id='myTable']/tbody/tr[1]/td[3]"))
            self.assertEqual("Row 0, cell 3", sel.get_text("//table[@id='myTable']/tbody/tr[1]/td[4]"))
            self.assertEqual("Row 1, cell 0", sel.get_text("//table[@id='myTable']/tbody/tr[2]/td[1]"))
            self.assertEqual("Row 1, cell 1", sel.get_text("//table[@id='myTable']/tbody/tr[2]/td[2]"))
            self.assertEqual("Row 1, cell 2", sel.get_text("//table[@id='myTable']/tbody/tr[2]/td[3]"))
            self.assertEqual("Row 1, cell 3", sel.get_text("//table[@id='myTable']/tbody/tr[2]/td[4]"))
            self.assertEqual("Row 2, cell 0", sel.get_text("//table[@id='myTable']/tbody/tr[3]/td[1]"))
            self.assertEqual("Row 2, cell 1", sel.get_text("//table[@id='myTable']/tbody/tr[3]/td[2]"))
            self.assertEqual("Row 2, cell 2", sel.get_text("//table[@id='myTable']/tbody/tr[3]/td[3]"))
            self.assertEqual("Row 2, cell 3", sel.get_text("//table[@id='myTable']/tbody/tr[3]/td[4]"))
            self.assertEqual("Row 3, cell 0", sel.get_text("//table[@id='myTable']/tbody/tr[4]/td[1]"))
            self.assertEqual("Row 3, cell 1", sel.get_text("//table[@id='myTable']/tbody/tr[4]/td[2]"))
            self.assertEqual("Row 3, cell 2", sel.get_text("//table[@id='myTable']/tbody/tr[4]/td[3]"))
            self.assertEqual("Row 3, cell 3", sel.get_text("//table[@id='myTable']/tbody/tr[4]/td[4]"))
            self.assertEqual("Row 4, cell 0", sel.get_text("//table[@id='myTable']/tbody/tr[5]/td[1]"))
            self.assertEqual("Row 4, cell 1", sel.get_text("//table[@id='myTable']/tbody/tr[5]/td[2]"))
            self.assertEqual("Row 4, cell 2", sel.get_text("//table[@id='myTable']/tbody/tr[5]/td[3]"))
            self.assertEqual("Row 4, cell 3", sel.get_text("//table[@id='myTable']/tbody/tr[5]/td[4]"))
    
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
