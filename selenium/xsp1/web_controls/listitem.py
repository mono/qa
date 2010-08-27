#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase


class WebControls_ListItem(xsp1TestCase):
    xsp1TestCaseId = 838898
    xsp2TestCaseId = 861793
    xsp4TestCaseId = None

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=listitem")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("ListItem test"))
            self.assertEqual("One", sel.get_selected_label("//*[@id=\"NumberList\"]"))
            sel.select("NumberList", "label=Two")
            self.assertEqual("Two", sel.get_selected_label("//*[@id=\"NumberList\"]"))
            sel.select("NumberList", "label=Five")
            self.assertEqual("Five", sel.get_selected_label("//*[@id=\"NumberList\"]"))
            sel.select("NumberList", "label=Eight")
            self.assertEqual("Eight", sel.get_selected_label("//*[@id=\"NumberList\"]"))
        except Exception,e:
            self.verificationErrors.append(str(e))

if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
