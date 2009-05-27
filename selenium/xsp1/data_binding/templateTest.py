#!/usr/bin/env python

import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class templateTest(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 840312
        else:
            self.testcaseid = 861689

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=databind-template")
            sel.wait_for_page_to_load("30000")
            try: self.assertEqual("odd", sel.get_text("//html/body/form/table/tbody/tr[6]/td/b"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.assertEqual("even", sel.get_text("//html/body/form/table/tbody/tr[5]/td/b"))
            except AssertionError, e: self.verificationErrors.append(str(e))

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:

