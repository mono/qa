#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.apache.apacheTestCase import apacheTestCase

class mvcTest(apacheTestCase):
    apacheTestCaseId = 872668
    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/mvcTest/")
            for i in range(60):
                try:
                    if sel.is_element_present("link=Home"): break
                except: pass
                time.sleep(1)
            sel.click("link=Home")
            self.assertEqual("Welcome to ASP.NET MVC!", sel.get_text("//div[@id='main']/h2"))
            for i in range(60):
                try:
                    if sel.is_element_present("link=About"): break
                except: pass
                time.sleep(1)
            sel.click("link=About")
            sel.wait_for_page_to_load("30000")
            self.assertEqual("About", sel.get_text("//div[@id='main']/h2"))
            self.assertEqual("Put content here.", sel.get_text("//div[@id='main']/p"))
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
