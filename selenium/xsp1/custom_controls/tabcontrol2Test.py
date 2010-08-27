#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase


class CustomControls_tabcontrolTest(xsp1TestCase):
    xsp1TestCaseId = 840314
    xsp2TestCaseId = 861724
    xsp4TestCaseId = None

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=tabcontrol2")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Image")
            sel.wait_for_page_to_load("30000")

            try:
                self.failUnless(sel.is_element_present("//*[@id=\"tabs_im\"]"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

            sel.click("link=Form")
            sel.wait_for_page_to_load("30000")
            sel.type("tabs_txt1", "You can write here. ahello")
            sel.click("tabs_btn")
            sel.wait_for_page_to_load("30000")

            try:
                self.failUnless(re.search(r"^[\s\S]*pressed me .* time[\s\S]*$", sel.get_text("//*[@id=\"tabs_uno\"]")))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

            sel.click("tabs_btn")
            sel.wait_for_page_to_load("30000")

            try:
                self.failUnless(re.search(r"^[\s\S]*pressed me .* times[\s\S]*$", sel.get_text("//*[@id=\"tabs_uno\"]")))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

            sel.type("tabs_txt1", "You can write here. ahellos")
            sel.click("tabs_btn")
            sel.wait_for_page_to_load("30000")

            try:
                self.failUnless(re.search(r"^[\s\S]*pressed me .* times[\s\S]*$", sel.get_text("//*[@id=\"tabs_uno\"]")))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

        except Exception,e:
            self.verificationErrors.append(str(e))

if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
