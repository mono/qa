#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase


class WebControls_WebDataGrid(xsp1TestCase):
    xsp1TestCaseId = 838902
    xsp2TestCaseId = 861963
    xsp4TestCaseId = None

    def _verifyRow(self, rowXPath, country, continent, abbr):
        self.assertEqual(country, self.selenium.get_text(rowXPath + "/td"))
        self.assertEqual(continent, self.selenium.get_text(rowXPath + "/td[2]"))
        self.assertEqual(abbr, self.selenium.get_text(rowXPath + "/td[3]"))
        

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_datagrid")
            sel.wait_for_page_to_load("30000")
            self.assertEqual("DataGrid sample", sel.get_text("//h3"))

            headerRowXPath = "//table[@id='dg']/tbody/tr"
            spainRowXPath = "//table[@id='dg']/tbody/tr[2]"
            japanRowXPath = "//table[@id='dg']/tbody/tr[3]"
            mexicoRowXPath = "//table[@id='dg']/tbody/tr[4]"

            self._verifyRow(headerRowXPath, "Country", "Continent", "Abbr")
            self._verifyRow(spainRowXPath, "Spain", "Europe", "es")
            self._verifyRow(japanRowXPath, "Japan", "Asia", "jp")
            self._verifyRow(mexicoRowXPath, "Mexico", "America", "mx")

        except Exception,e:
            print str(e)
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
