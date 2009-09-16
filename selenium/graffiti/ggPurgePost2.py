#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../..')
import common.monotesting as mono
from selenium.graffiti.graffitiTestCase import graffitiTestCase

class graffiti_gg_PurgePost2(graffitiTestCase):
    graffitiTestCaseId = 871075
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

            for i in range(60):
                try:
                    if sel.is_element_present("link=Posts"): break
                except: pass
                time.sleep(1)
            else: self.fail("time out")
            sel.click("link=Posts")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Deleted")
            sel.wait_for_page_to_load("30000")
            try:
                sel.click("link=Destroy")
            except:
                pass

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
