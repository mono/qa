#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase


class WebControls_Temperature(xsp1TestCase):
    xsp1TestCaseId = 839922
    xsp2TestCaseId = 861796

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=temperature")
            sel.wait_for_page_to_load("30000")
            sel.select("//*[@id=\"fromScale\"]", "Celsius")
            sel.type("degrees", "23")
            sel.select("//*[@id=\"toScale\"]", "Farenheit")
            sel.click("//*[@id=\"btn\"]")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_element_present("//*[@id=\"result\"]"))
            self.assertEqual("Converting 23 from Celsius to Farenheit gives 73.4", sel.get_text("result"))
            sel.select("//*[@id=\"fromScale\"]", "Farenheit")
            sel.type("degrees", "23")
            sel.select("//*[@id=\"toScale\"]", "Farenheit")
            sel.click("//*[@id=\"btn\"]")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_element_present("//*[@id=\"result\"]"))
            self.assertEqual("Converting 23 from Farenheit to Farenheit gives 23", sel.get_text("result"))
            sel.select("//*[@id=\"fromScale\"]", "Kelvin")
            sel.type("degrees", "23")
            sel.select("//*[@id=\"toScale\"]", "Farenheit")
            sel.click("//*[@id=\"btn\"]")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_element_present("//*[@id=\"result\"]"))
            self.assertEqual("Converting 23 from Kelvin to Farenheit gives -598", sel.get_text("result"))
            sel.select("//*[@id=\"fromScale\"]", "Kelvin")
            sel.type("degrees", "23")
            sel.select("//*[@id=\"toScale\"]", "Celsius")
            sel.click("//*[@id=\"btn\"]")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_element_present("//*[@id=\"result\"]"))
            self.assertEqual("Converting 23 from Kelvin to Celsius gives -350", sel.get_text("result"))
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
