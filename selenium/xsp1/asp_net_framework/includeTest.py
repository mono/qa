#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase


class AspNetFramework_includeTest(xsp1TestCase):
    xsp1TestCaseId = 838724
    xsp2TestCaseId = 861577

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=includetest")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("This is a default One!"))
            self.assertEqual("This is a default Two!", sel.get_text("Message2"))
            self.assertEqual("This is a label!", sel.get_text("Three"))

            if not mono.usexsp2:
                buttonName = "_ctl2"
            else:
                buttonName = "ctl02"
            sel.click(buttonName)

            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("Message text changed!"))
            try:
                self.failUnless(sel.is_text_present("Message text changed2!"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))
            self.failUnless(sel.is_text_present("Text changed!"))

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
