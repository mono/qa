#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class WebControls_WebDropDownList(xsp1TestCase):
    xsp1TestCaseId = 838903
    xsp2TestCaseId = 863176

    def test(self):
        if not self.canRun:
            return
        try:
            dropDownListXPath = "//*[@id=\"ddl\"]"
            labelXPath = "//*[@id=\"lbl\"]"
            buttonXPath = "//*[@id=\"btn\"]"
            
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_dropdownlist")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_element_present(dropDownListXPath))
            self.assertEqual("Item 1", sel.get_selected_label(dropDownListXPath))
            sel.click(buttonXPath)
            sel.wait_for_page_to_load("30000")
            self.assertEqual("You selected 'Item 1' (index #0).", sel.get_text(labelXPath))
            sel.select(dropDownListXPath, "label=Item 4")
            self.assertEqual("Item 4", sel.get_selected_label(dropDownListXPath))
            sel.click(buttonXPath)
            sel.wait_for_page_to_load("30000")
            self.assertEqual("You selected 'Item 4' (index #3).", sel.get_text(labelXPath))
            sel.select(dropDownListXPath, "label=Item 2")
            self.assertEqual("Item 2", sel.get_selected_label(dropDownListXPath))
            sel.click(buttonXPath)
            sel.wait_for_page_to_load("30000")
            self.assertEqual("You selected 'Item 2' (index #1).", sel.get_text(labelXPath))
            sel.select(dropDownListXPath, "label=Item 3")
            self.assertEqual("Item 3", sel.get_selected_label(dropDownListXPath))
            sel.click(buttonXPath)
            sel.wait_for_page_to_load("30000")
            self.assertEqual("You selected 'Item 3' (index #2).", sel.get_text(labelXPath))
        except Exception,e:
            self.verificationErrors.append(str(e))

if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
