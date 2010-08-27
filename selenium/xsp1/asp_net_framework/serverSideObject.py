#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase


class AspNetFramework_serverSideObject(xsp1TestCase):
    xsp1TestCaseId = 838725
    xsp2TestCaseId = 861580
    xsp4TestCaseId = None

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=server-side-object")
            sel.wait_for_page_to_load("30000")
            self.assertEqual("Here is a value: One", sel.get_text("//table[@id='MyList']/tbody/tr[1]/td"))
            self.assertEqual("Here is a value: Two", sel.get_text("//table[@id='MyList']/tbody/tr[2]/td"))
            self.assertEqual("Here is a value: Three", sel.get_text("//table[@id='MyList']/tbody/tr[3]/td"))
        except Exception,e:
            self.verificationErrors.append(str(e))

if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
