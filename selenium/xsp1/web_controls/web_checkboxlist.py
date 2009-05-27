#!/usr/bin/env python

import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class WebControls_WebCheckBoxList(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 838899 # xsp1 test case id
        else:
            self.testcaseid = 861803 # xsp2 test case id

    def _checkAndTest(self, sel, locator):
        self.failIf(sel.is_checked(locator))
        sel.click(locator)
        self.failUnless(sel.is_checked(locator))

    def _uncheckAndTest(self, sel, locator):
        self.failUnless(sel.is_checked(locator))
        sel.click(locator)
        self.failIf(sel.is_checked(locator))

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_checkboxlist")
            sel.wait_for_page_to_load("30000")

            flowOneXPath = "//*[@id=\"l1_0\"]"
            flowTwoXPath = "//*[@id=\"l1_1\"]"
            flowThreeXPath = "//*[@id=\"l1_2\"]"
            flowFiveXPath = "//*[@id=\"l1_3\"]"

            tableOneXPath = "//*[@id=\"l2_0\"]"
            tableTwoXPath = "//*[@id=\"l2_1\"]"
            tableThreeXPath = "//*[@id=\"l2_2\"]"
            tableFiveXPath = "//*[@id=\"l2_3\"]"

            # check, then uncheck all in order
            self._checkAndTest(sel, flowOneXPath)
            self._checkAndTest(sel, flowTwoXPath)
            self._checkAndTest(sel, flowThreeXPath)
            self._checkAndTest(sel, flowFiveXPath)

            self._checkAndTest(sel, tableOneXPath)
            self._checkAndTest(sel, tableTwoXPath)
            self._checkAndTest(sel, tableThreeXPath)
            self._checkAndTest(sel, tableFiveXPath)

            self._uncheckAndTest(sel, flowOneXPath)
            self._uncheckAndTest(sel, flowTwoXPath)
            self._uncheckAndTest(sel, flowThreeXPath)
            self._uncheckAndTest(sel, flowFiveXPath)

            self._uncheckAndTest(sel, tableOneXPath)
            self._uncheckAndTest(sel, tableTwoXPath)
            self._uncheckAndTest(sel, tableThreeXPath)
            self._uncheckAndTest(sel, tableFiveXPath)


            # check all in flow, then uncheck all in flow
            # check all in table, then uncheck all in table
            self._checkAndTest(sel, flowOneXPath)
            self._checkAndTest(sel, flowTwoXPath)
            self._checkAndTest(sel, flowThreeXPath)
            self._checkAndTest(sel, flowFiveXPath)

            self._uncheckAndTest(sel, flowOneXPath)
            self._uncheckAndTest(sel, flowTwoXPath)
            self._uncheckAndTest(sel, flowThreeXPath)
            self._uncheckAndTest(sel, flowFiveXPath)

            self._checkAndTest(sel, tableOneXPath)
            self._checkAndTest(sel, tableTwoXPath)
            self._checkAndTest(sel, tableThreeXPath)
            self._checkAndTest(sel, tableFiveXPath)

            self._uncheckAndTest(sel, tableOneXPath)
            self._uncheckAndTest(sel, tableTwoXPath)
            self._uncheckAndTest(sel, tableThreeXPath)
            self._uncheckAndTest(sel, tableFiveXPath)
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
