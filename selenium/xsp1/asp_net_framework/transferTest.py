#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase


class AspNetFramework_TransferTest(xsp1TestCase):
    xsp1TestCaseId = 837584
    xsp2TestCaseId = 861582
    xsp4TestCaseId = None

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=transfer1")
            sel.wait_for_page_to_load("30000")

            try:
                self.failUnless(sel.is_text_present("FilePath: /1.1/asp.net/transfer1.aspx"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

            try:
                self.failUnless(sel.is_text_present("CurrentExecutionFilePath: /1.1/asp.net/transfer2.aspx"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

        except AssertionError, e: self.verificationErrors.append(str(e))



if __name__ == "__main__":
    mono.monotesting_main()



# vim:ts=4:expandtab:
