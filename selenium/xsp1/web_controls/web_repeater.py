#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class WebControls_WebRepeater(xsp1TestCase):
    xsp1TestCaseId = 839934
    xsp2TestCaseId = 861807

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_repeater")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_element_present("//html/body/form/table"))
            self.assertEqual("Country", sel.get_text("//form[@id='_ctl1']/table/tbody/tr[1]/td[1]/b"))
            self.assertEqual("Abbreviation", sel.get_text("//form[@id='_ctl1']/table/tbody/tr[1]/td[2]/b"))
            self.assertEqual("Continent", sel.get_text("//form[@id='_ctl1']/table/tbody/tr[1]/td[3]/b"))
            self.assertEqual("Spain", sel.get_text("//form[@id='_ctl1']/table/tbody/tr[2]/td[1]"))
            self.assertEqual("es", sel.get_text("//form[@id='_ctl1']/table/tbody/tr[2]/td[2]"))
            self.assertEqual("Europe", sel.get_text("//form[@id='_ctl1']/table/tbody/tr[2]/td[3]"))
            self.assertEqual("Japan", sel.get_text("//form[@id='_ctl1']/table/tbody/tr[3]/td[1]"))
            self.assertEqual("jp", sel.get_text("//form[@id='_ctl1']/table/tbody/tr[3]/td[2]"))
            self.assertEqual("Asia", sel.get_text("//form[@id='_ctl1']/table/tbody/tr[3]/td[3]"))
            self.assertEqual("Mexico", sel.get_text("//form[@id='_ctl1']/table/tbody/tr[4]/td[1]"))
            self.assertEqual("mx", sel.get_text("//form[@id='_ctl1']/table/tbody/tr[4]/td[2]"))
            self.assertEqual("America", sel.get_text("//form[@id='_ctl1']/table/tbody/tr[4]/td[3]"))

        except Exception,e:
            self.verificationErrors.append(str(e))

if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
