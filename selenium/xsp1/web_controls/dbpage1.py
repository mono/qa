#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase


class WebControls_Dbpage1(xsp1TestCase):
    xsp1TestCaseId = 838897
    xsp2TestCaseId = 861730

    def test(self):
        if not self.canRun:
            return
        try:
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
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
