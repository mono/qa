#!/usr/bin/env python

import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class WebControls_ListItem(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 838898 # xsp1 test case id
        else:
            self.testcaseid = 861793 # xsp2 test case id

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=listitem")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("ListItem test"))
            self.assertEqual("One", sel.get_selected_label("//*[@id=\"NumberList\"]"))
            sel.select("NumberList", "label=Two")
            self.assertEqual("Two", sel.get_selected_label("//*[@id=\"NumberList\"]"))
            sel.select("NumberList", "label=Five")
            self.assertEqual("Five", sel.get_selected_label("//*[@id=\"NumberList\"]"))
            sel.select("NumberList", "label=Eight")
            self.assertEqual("Eight", sel.get_selected_label("//*[@id=\"NumberList\"]"))
        except Exception,e:
            self.verificationErrors.append(str(e))

if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
