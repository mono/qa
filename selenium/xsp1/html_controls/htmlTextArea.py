#!/usr/bin/env python

import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class HtmlControls_HtmlTextArea(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 838547
        else:
            self.testcaseid = 861720 

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=htmltextarea")
            sel.wait_for_page_to_load("30000")
            try: self.assertEqual("Hi there!\nCool!", sel.get_value("myTA"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.type("myTA", "Hi there!\nCool!\nSome additional text")
            try: self.assertEqual("Hi there!\nCool!\nSome additional text", sel.get_value("myTA"))
            except AssertionError, e: self.verificationErrors.append(str(e))

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
