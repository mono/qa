#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.apache.apacheTestCase import apacheTestCase

class MonoForums_cc_CreateThread(apacheTestCase):
    apacheTestCaseId = 510943
    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/AspNetForums/")
            sel.type("Loginbox1_ctl00_username", "test")
            sel.type("Loginbox1_ctl00_password", "test")
            sel.click("//*[@id=\"Loginbox1_ctl00_loginButton\"]")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Mono Forum")
            sel.wait_for_page_to_load("30000")
            sel.click("//*[@id=\"ctl01_ctl00_NewThreadImageTop\"]")
            sel.wait_for_page_to_load("30000")
            sel.type("Createeditpost1_PostForm_PostSubject", "Mono development")
            sel.type("Createeditpost1_PostForm_PostBody", "This is a new thread about mono development.")
            sel.click("Createeditpost1_PostForm_PostButton")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("Thread: Mono development"))
            self.failUnless(sel.is_text_present("This is a new thread about mono development."))
            self.assertEqual("test", sel.get_table("//table[@id='PostView1_ctl00_PostList']/tbody/tr[3]/td[1]/table.0.0"))

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
