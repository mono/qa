#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase


class AspNetFramework_typeDesc(xsp1TestCase):
    xsp1TestCaseId = 838728
    xsp2TestCaseId = 861583

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=typedesc")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("Passed!"))
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
