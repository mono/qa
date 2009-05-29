#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class WebControls_WebListBox(xsp1TestCase):
    xsp1TestCaseId = 838905
    xsp2TestCaseId = 861820
    MultiSelectLabel = "//*[@id=\"lbm\"]"
    SingleSelectLabel = "//*[@id=\"lbs\"]"

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_listbox")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("Single selection"))
            self.failUnless(sel.is_text_present("Multiple selection"))
            sel.select("lbs", "label=3")
            self.assertEqual("3", sel.get_selected_value(self.SingleSelectLabel))
            sel.select("lbs", "label=5")
            self.assertEqual("5", sel.get_selected_value(self.SingleSelectLabel))
            sel.add_selection("lbm", "label=2")
            self.assertEqual("2", sel.get_selected_value(self.MultiSelectLabel))
            sel.remove_selection("lbm", "label=2")
            sel.add_selection("lbm", "label=4")
            self.assertEqual("4", sel.get_selected_value(self.MultiSelectLabel))
            sel.add_selection("lbm", "label=1")
            self.assertEqual(["1", "4"], sel.get_selected_values(self.MultiSelectLabel))
            sel.remove_selection("lbm", "label=1")
            sel.remove_selection("lbm", "label=4")
            sel.add_selection("lbm", "label=5")
            sel.add_selection("lbm", "label=6")
            sel.add_selection("lbm", "label=7")
            sel.add_selection("lbm", "label=8")
            self.assertEqual(["5", "6", "7", "8"], sel.get_selected_values(self.MultiSelectLabel))
    
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
