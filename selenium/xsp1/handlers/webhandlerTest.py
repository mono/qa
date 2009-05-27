#!/usr/bin/env python

import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class Handlers_WebHandler(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 840264
        else:
            self.testcaseid = 861702 

    def test(self):
        if not self.canRun:
            return
        try: 

            def test(self):
                sel = self.selenium
                sel.open("/")
                sel.click("link=webhandler.ashx")
                sel.wait_for_page_to_load("30000")
                self.assertEqual("Hi there!", sel.get_text("//h1"))

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
