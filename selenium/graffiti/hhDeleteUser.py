#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../..')
import common.monotesting as mono
from selenium.graffiti.graffitiTestCase import graffitiTestCase

class graffiti_hh_deleteUser(graffitiTestCase):
    graffitiTestCaseId = 871076
    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            for i in range(60):
                try:
                    if sel.is_element_present("link=Login"): break
                except: pass
                time.sleep(1)
            else: self.fail("time out")
            sel.click("link=Login")
            sel.wait_for_page_to_load("30000")
            sel.type("UserName", "admin")
            sel.type("Password", "mono")
            sel.click("login")
            sel.wait_for_page_to_load("30000")
            sel.click("link=User Management")
            sel.wait_for_page_to_load("30000")
            sel.click("//div[@id='content']/div/div/div[1]/div[1]/div/div[2]")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Delete")
            for i in range(60):
                try:
                    if sel.is_element_present("ctl00_BodyRegion_DeleteUser"): break
                except: pass
                time.sleep(1)
            else: self.fail("time out")
            sel.click("ctl00_BodyRegion_DeleteUser")
            sel.wait_for_page_to_load("30000")
            sel.click("//div[@id='content']/div/div/div[1]/div[1]/div/div[2]")
            sel.wait_for_page_to_load("30000")
            self.failIf(sel.is_text_present("mono user"))
            sel.click("link=Log Off")
            sel.wait_for_page_to_load("30000")

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
