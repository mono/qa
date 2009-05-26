#!/usr/bin/env python


import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class AspNetFramework_browserCaps(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 838720
        else:
            self.testcaseid = 861573

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=browsercaps")
            sel.wait_for_page_to_load("30000")
            try:
                self.assertEqual("False", sel.get_text("//table[@id='dg']/tbody/tr[2]/td[2]"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

            try:
                self.assertEqual("Firefox", sel.get_text("//table[@id='dg']/tbody/tr[6]/td[2]"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

            try:
                self.assertEqual("True", sel.get_text("//table[@id='dg']/tbody/tr[19]/td[2]"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

            try:
                self.assertEqual("System.Web.UI.HtmlTextWriter", sel.get_text("//table[@id='dg']/tbody/tr[20]/td[2]"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

        except Exception,e:
            self.verificationErrors.append(str(e))

if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
