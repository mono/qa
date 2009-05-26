#!/usr/bin/env python


import sys
sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class AspNetFramework_RegisterTest(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 837574 # xsp1 test case id
        else:
            self.testcaseid = 861578 # xsp2 test case id

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=registertest")
            sel.wait_for_page_to_load("30000")

            # test the initial text to make sure it's what we think it should be
            try:
                self.assertEqual("This is a default One!", sel.get_text("//*[@id=\"Message\"]"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

            try:
                self.assertEqual("This is a default Two!", sel.get_text("//*[@id=\"Message2\"]"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

            try:
                self.assertEqual("This is a label!", sel.get_text("//*[@id=\"Three\"]"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

            for ix in range(2):
                # click the "Change" button and make sure the text changes
                sel.click("//html/body/form/p[3]/input")
                sel.wait_for_page_to_load("30000")

                try:
                    self.assertEqual("Message text changed!", sel.get_text("//*[@id=\"Message\"]"))
                except AssertionError, e:
                    self.verificationErrors.append(str(e))

                try:
                    self.assertEqual("Message text changed2!", sel.get_text("//*[@id=\"Message2\"]"))
                except AssertionError, e:
                    self.verificationErrors.append(str(e))

                try:
                    self.assertEqual("Text changed!", sel.get_text("//*[@id=\"Three\"]"))
                except AssertionError, e:
                    self.verificationErrors.append(str(e))

        except AssertionError, e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()



# vim:ts=4:expandtab:
