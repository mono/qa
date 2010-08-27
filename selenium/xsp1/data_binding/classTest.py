#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class classTest (xsp1TestCase):
    xsp1TestCaseId = 840313
    xsp2TestCaseId = 861688
    xsp4TestCaseId = None

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=databind-class")
            sel.wait_for_page_to_load("30000")
            sel.select("list", "label=Two")
            sel.wait_for_page_to_load("30000")
            try: self.assertEqual("Selected option: Two 2", sel.get_text("//*[@id=\"msg\"]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.select("list", "label=Five")
            sel.wait_for_page_to_load("30000")
            try: self.assertEqual("Selected option: Five 5", sel.get_text("//*[@id=\"msg\"]"))
            except AssertionError, e: self.verificationErrors.append(str(e))

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
