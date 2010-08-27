#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class HtmlControls_HtmlAnchor(xsp1TestCase):
    xsp1TestCaseId = 838535
    xsp2TestCaseId = 861706

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=htmlanchor")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("Go mono!"))
            sel.click("myAnchor")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("Mono"))
            self.failUnless(sel.is_text_present(".NET"))
            self.failUnless(sel.is_text_present("C#"))

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
