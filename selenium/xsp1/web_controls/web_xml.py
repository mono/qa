#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class WebControls_WebXML(xsp1TestCase):
    xsp1TestCaseId = 838910
    xsp2TestCaseId = 861811
    xsp4TestCaseId = None

    def ControlXPath(self, tbl, td):
        if not mono.usexsp2:
            self.FormCtl = "_ctl1"
        else:
            self.FormCtl = "ctl01"
        return "//form[@id='" + self.FormCtl + "']/table[" + tbl + "]/tbody/tr[" + td + "]/td"

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_xml")
            sel.wait_for_page_to_load("30000")
            self.assertEqual("Xml Example", sel.get_text("//h3"))
            self.assertEqual("Joe   Suits", sel.get_text(self.ControlXPath("1", "1")))
            self.assertEqual("Job Title: CEO\n Description: Wears the nice suit", sel.get_text(self.ControlXPath("1", "3")))
            self.assertEqual("Jeremy   Boards", sel.get_text(self.ControlXPath("3", "1")))
            self.assertEqual("Job Title: Pro Surfer\n Description: Rides the big waves", sel.get_text(self.ControlXPath("3", "3")))
            self.assertEqual("Joan   Page", sel.get_text(self.ControlXPath("4", "1")))
            self.assertEqual("Job Title: Web Site Developer\n Description: Writes the pretty pages", sel.get_text(self.ControlXPath("4", "3")))
  
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
