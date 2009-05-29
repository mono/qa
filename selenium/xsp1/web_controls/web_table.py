#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class WebControls_WebTable(xsp1TestCase):
    xsp1TestCaseId = 838909
    xsp2TestCaseId = 861809

    def TableXPath(self, tr, td):
        return "//table[@id='myTable']/tbody/tr[" + tr + "]/td[" + td + "]"

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_table")
            sel.wait_for_page_to_load("30000")
            self.assertEqual("Row 0, cell 0", sel.get_text(self.TableXPath("1", "1")))
            self.assertEqual("Row 0, cell 1", sel.get_text(self.TableXPath("1", "2")))
            self.assertEqual("Row 0, cell 2", sel.get_text(self.TableXPath("1", "3")))
            self.assertEqual("Row 0, cell 3", sel.get_text(self.TableXPath("1", "4")))
            self.assertEqual("Row 1, cell 0", sel.get_text(self.TableXPath("2", "1")))
            self.assertEqual("Row 1, cell 1", sel.get_text(self.TableXPath("2", "2")))
            self.assertEqual("Row 1, cell 2", sel.get_text(self.TableXPath("2", "3")))
            self.assertEqual("Row 1, cell 3", sel.get_text(self.TableXPath("2", "4")))
            self.assertEqual("Row 2, cell 0", sel.get_text(self.TableXPath("3", "1")))
            self.assertEqual("Row 2, cell 1", sel.get_text(self.TableXPath("3", "2")))
            self.assertEqual("Row 2, cell 2", sel.get_text(self.TableXPath("3", "3")))
            self.assertEqual("Row 2, cell 3", sel.get_text(self.TableXPath("3", "4")))
            self.assertEqual("Row 3, cell 0", sel.get_text(self.TableXPath("4", "1")))
            self.assertEqual("Row 3, cell 1", sel.get_text(self.TableXPath("4", "2")))
            self.assertEqual("Row 3, cell 2", sel.get_text(self.TableXPath("4", "3")))
            self.assertEqual("Row 3, cell 3", sel.get_text(self.TableXPath("4", "4")))
            self.assertEqual("Row 4, cell 0", sel.get_text(self.TableXPath("5", "1")))
            self.assertEqual("Row 4, cell 1", sel.get_text(self.TableXPath("5", "2")))
            self.assertEqual("Row 4, cell 2", sel.get_text(self.TableXPath("5", "3")))
            self.assertEqual("Row 4, cell 3", sel.get_text(self.TableXPath("5", "4")))
    
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
