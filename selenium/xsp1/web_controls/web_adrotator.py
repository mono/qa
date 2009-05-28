#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase


class WebControls_WebAdRotator(xsp1TestCase):
    xsp1TestCaseId = 839924
    xsp2TestCaseId = 861798

    def _runDancingMonkeyAd(self):
        while not self.selenium.is_element_present("//img[@alt='Dancing monkey']"):
            try:
                self.failUnless(self.selenium.is_element_present("//img[@alt='Mono']"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))
            self.selenium.refresh()
            self.selenium.wait_for_page_to_load("30000")

        self.selenium.click("//html/body/form/a/img")
        self.selenium.wait_for_page_to_load("30000")

        # we don't know if the title for the novell.com/linux page will always be "Linux OS"
        #self.assertEqual("Linux OS | SUSE Linux Enterprise", self.selenium.get_title())

        self.failUnless(self.selenium.is_element_present("//html/body"))
        self.selenium.go_back()
        self.selenium.wait_for_page_to_load("30000")

    def _runMonoAd(self):
        while not self.selenium.is_element_present("//img[@alt='Mono']"):
            try:
                self.failUnless(self.selenium.is_element_present("//img[@alt='Dancing monkey']"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))
            self.selenium.refresh()
            self.selenium.wait_for_page_to_load("30000")

        self.selenium.click("//html/body/form/a/img")
        self.selenium.wait_for_page_to_load("30000")
        self.assertEqual("Main Page - Mono", self.selenium.get_title())
        self.selenium.go_back()
        self.selenium.wait_for_page_to_load("30000")

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_adrotator")
            sel.wait_for_page_to_load("30000")

            for ix in range(5):
                self._runDancingMonkeyAd()
                self._runMonoAd()

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
