#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class Handlers_WebHandler (xsp1TestCase):
    xsp1TestCaseId = 840264
    xsp2TestCaseId = 861702
    xsp4TestCaseId = None

    def test(self):
        HeadingXpath = "//h1"
        if not self.canRun:
            return
        try: 
            sel = self.selenium
            sel.open("/")
            sel.click("link=webhandler.ashx")
            sel.wait_for_page_to_load("30000")
            self.assertEqual("Hi there!", sel.get_text(HeadingXpath))

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
