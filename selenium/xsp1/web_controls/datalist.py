#!/usr/bin/env python


import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class WebControls_DataList(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 838896 # xsp1 test case id
        else:
            self.testcaseid = 861729 # xsp2 test case id

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=datalist")
            sel.wait_for_page_to_load("30000")

            try:
                self.assertEqual("Datalist sample", sel.get_text("//h3"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

            self.assertEqual("Spain", sel.get_text("//table[@id='dl']/tbody/tr/td[1]/span"))
            self.assertEqual("Japan", sel.get_text("//table[@id='dl']/tbody/tr/td[2]/span"))
            self.assertEqual("Mexico", sel.get_text("//table[@id='dl']/tbody/tr/td[3]/span"))
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
