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
            self.assertEqual("off", sel.get_value("rb1"))
            self.assertEqual("off", sel.get_value("rb2"))
            self.assertEqual("on", sel.get_value("rb3"))
            self.assertEqual("off", sel.get_value("rb4"))
            self.assertEqual("on", sel.get_value("rb5"))
            sel.click("rb1")
            self.assertEqual("on", sel.get_value("rb1"))
            self.assertEqual("off", sel.get_value("rb2"))
            self.assertEqual("off", sel.get_value("rb3"))
            self.assertEqual("off", sel.get_value("rb4"))
            self.assertEqual("on", sel.get_value("rb5"))
            sel.click("rb2")
            self.assertEqual("off", sel.get_value("rb1"))
            self.assertEqual("on", sel.get_value("rb2"))
            self.assertEqual("off", sel.get_value("rb3"))
            self.assertEqual("off", sel.get_value("rb4"))
            self.assertEqual("on", sel.get_value("rb5"))
            sel.click("rb3")
            self.assertEqual("", sel.get_text("rb1"))
            self.assertEqual("off", sel.get_value("rb2"))
            self.assertEqual("on", sel.get_value("rb3"))
            self.assertEqual("off", sel.get_value("rb4"))
            self.assertEqual("on", sel.get_value("rb5"))
            sel.click("rb4")
            self.assertEqual("off", sel.get_value("rb1"))
            self.assertEqual("off", sel.get_value("rb2"))
            self.assertEqual("on", sel.get_value("rb3"))
            self.assertEqual("on", sel.get_value("rb4"))
            self.assertEqual("off", sel.get_value("rb5"))
            sel.click("rb5")
            self.assertEqual("off", sel.get_value("rb1"))
            self.assertEqual("off", sel.get_value("rb2"))
            self.assertEqual("on", sel.get_value("rb3"))
            self.assertEqual("off", sel.get_value("rb4"))
            self.assertEqual("on", sel.get_value("rb5"))
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
