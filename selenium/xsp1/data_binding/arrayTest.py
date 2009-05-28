#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class DataBinding_ArrayTest(xsp1TestCase):
    xsp1TestCaseId = 839038
    xsp2TestCaseId = 861685

    def test(self):
        if not self.canRun:
            return
        try: 
            sel = self.selenium
            sel.open("/")
            sel.click("link=databind-arraylist")
            sel.wait_for_page_to_load("30000")
            sel.select("list", "label=Two")
            sel.wait_for_page_to_load("30000")
            try: self.assertEqual("Selected option: Two", sel.get_text("//*[@id=\"msg\"]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.select("list", "label=Four")
            sel.wait_for_page_to_load("30000")
            try: self.assertEqual("Selected option: Four", sel.get_text("//*[@id=\"msg\"]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.select("list", "label=One")
            sel.wait_for_page_to_load("30000")
            try: self.assertEqual("Selected option: One", sel.get_text("//*[@id=\"msg\"]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
