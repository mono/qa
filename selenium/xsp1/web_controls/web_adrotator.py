#!/usr/bin/env python

import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class WebControls_WebAdRotator(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 839924 # xsp1 test case id
        else:
            self.testcaseid = 861798 # xsp2 test case id

    def _runDancingMonkeyAd(self, sel):
        while not sel.is_element_present("//img[@alt='Dancing monkey']"):
            try:
                self.failUnless(sel.is_element_present("//img[@alt='Mono']"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))
            sel.refresh()
            sel.wait_for_page_to_load("30000")

        sel.click("//html/body/form/a/img")
        sel.wait_for_page_to_load("30000")

        # we don't know if the title for the novell.com/linux page will always be "Linux OS"
        #self.assertEqual("Linux OS | SUSE Linux Enterprise", sel.get_title())

        self.failUnless(sel.is_element_present("//html/body"))
        sel.go_back()
        sel.wait_for_page_to_load("30000")

    def _runMonoAd(self, sel):
        while not sel.is_element_present("//img[@alt='Mono']"):
            try:
                self.failUnless(sel.is_element_present("//img[@alt='Dancing monkey']"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))
            sel.refresh()
            sel.wait_for_page_to_load("30000")

        sel.click("//html/body/form/a/img")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Main Page - Mono", sel.get_title())
        sel.go_back()
        sel.wait_for_page_to_load("30000")

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_adrotator")
            sel.wait_for_page_to_load("30000")

            for ix in range(5):
                self._runDancingMonkeyAd(sel)
                self._runMonoAd(sel)

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
