#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class templateTest (xsp1TestCase):
    xsp1TestCaseId = 840312
    xsp2TestCaseId = 861689

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

