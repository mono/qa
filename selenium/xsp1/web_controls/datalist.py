#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase


class WebControls_DataList(xsp1TestCase):
    xsp1TestCaseId = 838896
    xsp2TestCaseId = 861729
    xsp4TestCaseId = None

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
