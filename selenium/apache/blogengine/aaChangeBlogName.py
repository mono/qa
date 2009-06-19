#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.apache.apacheTestCase import apacheTestCase

class blogengine_aa_ChangeBlogName(apacheTestCase):
    apacheTestCaseId = None
    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/blogengine/")
            sel.click("ctl00_aLogin")
            sel.wait_for_page_to_load("30000")
            sel.type("ctl00_cphBody_Login1_UserName", "admin")
            sel.type("ctl00_cphBody_Login1_Password", "admin")
            sel.click("ctl00_cphBody_Login1_LoginButton")
            sel.wait_for_page_to_load("30000")
            sel.click("//ul[@id='ctl00_42fcbe7c2c9c440abad965a94472fccc_uxMenu_ulMenu']/li[7]/a/span")
            sel.wait_for_page_to_load("30000")
            sel.type("ctl00_cphAdmin_txtName", "Mono Blog")
            sel.type("ctl00_cphAdmin_txtDescription", "Discussions about mono")
            sel.click("ctl00_cphAdmin_btnSave")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Go to front page")
            sel.wait_for_page_to_load("30000")
            self.assertEqual("Mono Blog", sel.get_text("link=Mono Blog"))
            sel.click("link=Log off")
            sel.wait_for_page_to_load("30000")

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
