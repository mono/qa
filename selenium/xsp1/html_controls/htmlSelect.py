#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class HtmlControls_HtmlSelect(xsp1TestCase):
    xsp1TestCaseId = 838545
    xsp2TestCaseId = 861718
    xsp4TestCaseId = None

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=htmlselect")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("Select a language:"))
            self.failUnless(sel.is_element_present("//*[@id=\"lselect\"]"))
            self.assertEqual("C", sel.get_selected_label("lselect"))
            sel.select("lselect", "label=C++")
            self.assertEqual("C++", sel.get_selected_label("lselect"))

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
