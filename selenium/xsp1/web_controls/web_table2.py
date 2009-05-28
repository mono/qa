#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class WebControls_WebTable2(xsp1TestCase):
    xsp1TestCaseId = 839935
    xsp2TestCaseId = 861808

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_table2")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_element_present("//html/body/form/table"))
            self.assertEqual("TEST", sel.get_text("//form[@id='_ctl1']/table/tbody/tr/td"))

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
