#!/usr/bin/env python

import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class classTest(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 840313
        else:
            self.testcaseid = 861688 

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
