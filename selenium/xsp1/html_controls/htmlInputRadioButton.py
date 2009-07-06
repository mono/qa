#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class HtmlControls_HtmlInputRadioButton(xsp1TestCase):
    xsp1TestCaseId = 838544
    xsp2TestCaseId = 861716

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=htmlinputradiobutton")
            sel.wait_for_page_to_load("30000")
            if not mono.usexsp2:
                self.assertEqual("One\n Two\n Three\n One bis\n Two bis", sel.get_text("_ctl1"))
            else:
                #self.assertEqual("//<![CDATA[ var theForm; if (document.getElementById) { theForm = document.getElementById ('ctl01'); } else { theForm = document.ctl01; } //]]> \n One\n Two\n Three\n One bis\n Two bis", sel.get_text("ctl01"))
                self.assertEqual("One\n Two\n Three\n One bis\n Two bis", sel.get_text("ctl01"))
            self.failUnless(sel.is_checked("//*[@id=\"rb3\"]"))
            sel.click("rb1")
            self.failIf(sel.is_checked("//*[@id=\"rb3\"]"))
            self.failUnless(sel.is_checked("//*[@id=\"rb5\"]"))
            sel.click("rb4")
            self.failIf(sel.is_checked("//*[@id=\"rb5\"]"))

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
