#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class HtmlControls_HtmlTextArea(xsp1TestCase):
    xsp1TestCaseId = 838547
    xsp2TestCaseId = 861720
    xsp4TestCaseId = None

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=htmltextarea")
            sel.wait_for_page_to_load("30000")
            try: self.assertEqual("Hi there!\nCool!", sel.get_value("myTA"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.type("myTA", "Hi there!\nCool!\nSome additional text")
            try: self.assertEqual("Hi there!\nCool!\nSome additional text", sel.get_value("myTA"))
            except AssertionError, e: self.verificationErrors.append(str(e))

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
