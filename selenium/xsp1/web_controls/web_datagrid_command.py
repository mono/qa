#!/usr/bin/env python

import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class WebControls_WebDataGridCommand(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 839926 # xsp1 test case id
        else:
            self.testcaseid = 861806 # xsp2 test case id

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_datagrid_command")
            sel.wait_for_page_to_load("30000")
            self.assertEqual("Spain", sel.get_text("//table[@id='dg']/tbody/tr[2]/td[2]"))
            self.assertEqual("Japan", sel.get_text("//table[@id='dg']/tbody/tr[3]/td[2]"))
            self.assertEqual("Austria", sel.get_text("//table[@id='dg']/tbody/tr[4]/td[2]"))
            self.assertEqual("France", sel.get_text("//table[@id='dg']/tbody/tr[5]/td[2]"))
            self.assertEqual("Great Britain", sel.get_text("//table[@id='dg']/tbody/tr[6]/td[2]"))
            self.assertEqual("Italia", sel.get_text("//table[@id='dg']/tbody/tr[7]/td[2]"))
            self.assertEqual("India", sel.get_text("//table[@id='dg']/tbody/tr[8]/td[2]"))
            self.assertEqual("Brazil", sel.get_text("//table[@id='dg']/tbody/tr[9]/td[2]"))
            self.assertEqual("Germany", sel.get_text("//table[@id='dg']/tbody/tr[10]/td[2]"))
            self.assertEqual("Mexico", sel.get_text("//table[@id='dg']/tbody/tr[11]/td[2]"))
            self.assertEqual("Europe", sel.get_text("//table[@id='dg']/tbody/tr[2]/td[3]"))
            self.assertEqual("Asia", sel.get_text("//table[@id='dg']/tbody/tr[8]/td[3]"))
            self.assertEqual("mx", sel.get_text("//table[@id='dg']/tbody/tr[11]/td[4]"))
            self.assertEqual("jp", sel.get_text("//table[@id='dg']/tbody/tr[3]/td[4]"))
            sel.click("//html/body/form/table/tbody/tr[2]/td/a")
            sel.wait_for_page_to_load("30000")
            sel.click("//html/body/form/table/tbody/tr[10]/td/a")
            sel.wait_for_page_to_load("30000")
            sel.click("//html/body/form/table/tbody/tr[7]/td/a")
            sel.wait_for_page_to_load("30000")
            sel.click("//html/body/form/table/tbody/tr[6]/td/a")
            sel.wait_for_page_to_load("30000")
            sel.click("//html/body/form/table/tbody/tr[4]/td/a")
            sel.wait_for_page_to_load("30000")
            sel.click("//html/body/form/table/tbody/tr[2]/td/a")
            sel.wait_for_page_to_load("30000")
            sel.click("//html/body/form/table/tbody/tr[4]/td/a")
            sel.wait_for_page_to_load("30000")
            sel.click("//html/body/form/table/tbody/tr[3]/td/a")
            sel.wait_for_page_to_load("30000")
            sel.click("//html/body/form/table/tbody/tr[2]/td/a")
            sel.wait_for_page_to_load("30000")
            sel.click("//html/body/form/table/tbody/tr[2]/td/a")
            sel.wait_for_page_to_load("30000")
        except Exception,e:
            self.verificationErrors.append(str(e))

if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
