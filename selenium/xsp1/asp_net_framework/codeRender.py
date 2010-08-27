#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase


class AspNetFramework_codeRender(xsp1TestCase):
    xsp1TestCaseId = 838722
    xsp2TestCaseId = 861576
    xsp4TestCaseId = None

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=code-render")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("hi! message number 0."))
            self.failUnless(sel.is_text_present("hello message number 1."))
            self.failUnless(sel.is_text_present("hola message number 2."))
            self.failUnless(sel.is_text_present("Ciao message number 3."))
            self.failUnless(sel.is_text_present("adios message number 4."))
            sel.click("link=14")
            sel.wait_for_page_to_load("30000")
            sel.click("link=16")
            sel.wait_for_page_to_load("30000")
            sel.click("link=>")
            sel.wait_for_page_to_load("30000")
            sel.click("link=<")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("This should say hello: hello"))
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
