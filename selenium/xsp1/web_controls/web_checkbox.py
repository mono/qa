#!/usr/bin/env python

import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class WebControls_WebCheckBox(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 838900 # xsp1 test case id
        else:
            self.testcaseid = 861804 # xsp2 test case id

    def _checkCheckbox(self, sel, locator):
        self.failUnless(sel.is_element_present(locator))
        self.failIf(sel.is_checked(locator))
        sel.check(locator)
        self.failUnless(sel.is_checked(locator))

    def _uncheckCheckbox(self, sel, locator):
        self.failUnless(sel.is_element_present(locator))
        self.failUnless(sel.is_checked(locator))
        sel.uncheck(locator)
        self.failIf(sel.is_checked(locator))

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_checkbox")
            sel.wait_for_page_to_load("30000")

            clickHereXPath = "//*[@id=\"chk\"]"
            clickAlsoHereXPath = "//*[@id=\"chk2\"]"

            # Check / uncheck all in order
            self._checkCheckbox(sel, clickHereXPath)
            self._checkCheckbox(sel, clickAlsoHereXPath)

            self._uncheckCheckbox(sel, clickHereXPath)
            self._uncheckCheckbox(sel, clickAlsoHereXPath)

            # Check / uncheck one, then the other
            self._checkCheckbox(sel, clickHereXPath)
            self._uncheckCheckbox(sel, clickHereXPath)

            self._checkCheckbox(sel, clickAlsoHereXPath)
            self._uncheckCheckbox(sel, clickAlsoHereXPath)

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
