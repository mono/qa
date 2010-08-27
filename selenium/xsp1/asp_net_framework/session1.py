#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase


class AspNetFramework_session1(xsp1TestCase):
    xsp1TestCaseId = 838727
    xsp2TestCaseId = 861581
    xsp4TestCaseId = None

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=session1")
            sel.wait_for_page_to_load("30000")
            self.assertEqual("You can write here.", sel.get_text("txt1"))
            sel.type("txt1", "This is new text.")
            sel.click("btn")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("Somebody pressed me"))
            self.failUnless(sel.is_text_present("Text have changed"))
            sel.click("btn")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("Somebody pressed me"))
            sel.type("txt1", "This is more new text.")
            sel.click("btn")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("Somebody pressed me"))
            self.failUnless(sel.is_text_present("Text have changed"))
            self.failUnless(sel.is_text_present("This is more new text."))
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
