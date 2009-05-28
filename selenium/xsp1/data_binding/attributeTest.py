#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class DataBinding_AttributeTest (xsp1TestCase):
    xsp1TestCaseId = 839039
    xsp2TestCaseId = 861686

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=databind-attribute")
            sel.wait_for_page_to_load("30000")
            sel.select("list", "label=Two")
            sel.wait_for_page_to_load("30000")

            try:
                self.assertEqual("Two", sel.get_text("//*[@id=\"msg\"]"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

            sel.select("list", "label=One")
            sel.wait_for_page_to_load("30000")

            try:
                self.assertEqual("One", sel.get_text("//*[@id=\"msg\"]"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

            sel.select("list", "label=Five")
            sel.wait_for_page_to_load("30000")

            try:
                self.assertEqual("Five", sel.get_text("//*[@id=\"msg\"]"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
