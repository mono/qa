#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase


class WebControls_WebHyperLink(xsp1TestCase):
    xsp1TestCaseId = 839927
    xsp2TestCaseId = 863229
    xsp4TestCaseId = None

    def test(self):
        if not self.canRun:
            return
        try:
            imageXPath = "//img[@alt='Ximian']"

            sel = self.selenium
            sel.open("/")
            sel.click("link=web_hyperlink")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_element_present(imageXPath))
            sel.click(imageXPath)
            sel.wait_for_page_to_load("30000")
            self.assertEqual("Ximian", sel.get_title())
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
