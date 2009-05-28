#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase


class WebControls_Dbpage2(xsp1TestCase):
    xsp1TestCaseId = 840269
    xsp2TestCaseId = 861785

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=dbpage2")
            sel.wait_for_page_to_load("30000")
            self.assertEqual("Joe Doe", sel.get_text("//table[@id='tabs_browse']/tbody/tr[1]/td[2]"))
            self.assertEqual("The Swamp, 12314", sel.get_text("//table[@id='tabs_browse']/tbody/tr[5]/td[3]"))
            sel.click("link=Insert")
            sel.wait_for_page_to_load("30000")
            sel.type("tabs_dbID", "1234")
            sel.type("tabs_dbName", "Rupert Monkey")
            sel.type("tabs_dbAddress", "Mono Town")
            sel.click("tabs_insertSubmit")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Browse")
            sel.wait_for_page_to_load("30000")
            self.assertEqual("1234", sel.get_text("//table[@id='tabs_browse']/tbody/tr[6]/td[1]"))
            self.assertEqual("Rupert Monkey", sel.get_text("//table[@id='tabs_browse']/tbody/tr[6]/td[2]"))
            self.assertEqual("Mono Town", sel.get_text("//table[@id='tabs_browse']/tbody/tr[6]/td[3]"))
            sel.click("link=Update")
            sel.wait_for_page_to_load("30000")
            sel.type("tabs_updateID", "1234")
            sel.type("tabs_updateName", "Rupert Ximian")
            sel.type("tabs_updateAddress", "South Mono Town")
            sel.click("tabs_updateSubmit")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Browse")
            sel.wait_for_page_to_load("30000")
            self.assertEqual("1234", sel.get_text("//table[@id='tabs_browse']/tbody/tr[6]/td[1]"))
            self.assertEqual("Rupert Ximian", sel.get_text("//table[@id='tabs_browse']/tbody/tr[6]/td[2]"))
            self.assertEqual("South Mono Town", sel.get_text("//table[@id='tabs_browse']/tbody/tr[6]/td[3]"))
            sel.click("link=Delete")
            sel.wait_for_page_to_load("30000")
            sel.type("tabs_deleteID", "1234")
            sel.click("tabs_deleteSubmit")
            sel.wait_for_page_to_load("30000")
            sel.click("tabs_confirmDelete")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Browse")
            sel.wait_for_page_to_load("30000")

            try:
                self.failIf(sel.is_text_present("Rupert Ximian"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

            try:
                self.failIf(sel.is_text_present("South Mono Town"))
            except AssertionError, e:
                self.verificationErrors.append(str(e))

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
