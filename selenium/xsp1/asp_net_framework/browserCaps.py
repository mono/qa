#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class AspNetFramework_browserCaps(xsp1TestCase):
    xsp1TestCaseId = 838720
    xsp2TestCaseId = 861573

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=browsercaps")
            sel.wait_for_page_to_load("30000")
            try:
                # The following xpath refers to the "ActiveXControls" "False" table entry
                activeXControlsXPath = "//table[@id='dg']/tbody/tr[2]/td[2]"

                self.assertEqual("False", sel.get_text(activeXControlsXPath))
            except AssertionError, e:
                self.verificationErrors.append("ActiveXControls test: " + str(e))

            try:
                # The following xpath refers to the "Browser" "Firefox" table entry
                if not mono.usexsp2:
                    browserXPath = "//table[@id='dg']/tbody/tr[6]/td[2]"
                else:
                    browserXPath = "//table[@id='dg']/tbody/tr[7]/td[2]"
                browser_txt = sel.get_text(browserXPath)
                if browser_txt == "Firefox" or browser_txt == "Mozilla":
                    txt_ok = "True"
                else:
                    txt_ok = "False"
                print(browser_txt + browserXPath)
                self.assertEqual(txt_ok, "True")
            except AssertionError, e:
                self.verificationErrors.append("Browser test: " + str(e))

            try:
                # The following xpath refers to the "Tables" "True" table entry
                if not mono.usexsp2:
                    tablesXPath = "//table[@id='dg']/tbody/tr[20]/td[2]"
                else:
                    tablesXPath = "//table[@id='dg']/tbody/tr[107]/td[2]"

                self.assertEqual("True", sel.get_text(tablesXPath))
            except AssertionError, e:
                self.verificationErrors.append("Tables test: " + str(e))

            try:
                # The following xpath refers to the "TagWriter" "System.Web.UI.HtmlTextWriter" table entry
                if not mono.usexsp2:
                    tagWriterXPath = "//table[@id='dg']/tbody/tr[21]/td[2]"
                else:
                    tagWriterXPath = "//table[@id='dg']/tbody/tr[108]/td[2]"

                self.assertEqual("System.Web.UI.HtmlTextWriter", sel.get_text(tagWriterXPath))
            except AssertionError, e:
                self.verificationErrors.append("System.Web.UI.HtmlTextWriter test: " + str(e))

        except Exception,e:
            self.verificationErrors.append(str(e))

if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
