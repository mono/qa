#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class HtmlControls_HtmlInputFile(xsp1TestCase):
    xsp1TestCaseId = 838541
    xsp2TestCaseId = 861713

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=htmlinputfile")
            sel.wait_for_page_to_load("30000")
            sel.type("myFile", "test.jpg")
            sel.click("smt")
            sel.wait_for_page_to_load("30000")
            try: self.failUnless(sel.is_text_present("Pick a JPEG file"))
            except AssertionError, e: self.verificationErrors.append(str(e))
    
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
