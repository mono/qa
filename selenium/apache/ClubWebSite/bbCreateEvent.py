#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.apache.apacheTestCase import apacheTestCase

class aaCreateCategory(apacheTestCase):
    apacheTestCaseId = None
    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/ClubWebSite/")
            sel.type("ctl00_ContentPlaceHolder1_lv1_Login1_UserName", "test")
            sel.type("ctl00_ContentPlaceHolder1_lv1_Login1_Password", "test")
            sel.click("ctl00_ContentPlaceHolder1_lv1_Login1_RememberMe")
            sel.click("ctl00_ContentPlaceHolder1_lv1_Login1_LoginButton")
            sel.click("ctl00_TopNavRepeat_ctl02_HyperLink1")
            sel.wait_for_page_to_load("30000")
            sel.click("ctl00_ContentPlaceHolder1_Addbtn")
            sel.wait_for_page_to_load("30000")
            sel.type("ctl00_ContentPlaceHolder1_FormView1_titleTextBox", "Mono Summit in Down Under")
            sel.select("ctl00_ContentPlaceHolder1_FormView1_LocationPicker1_locationselect", "label=New Zealand")
            sel.click("//option[@value='3']")
            sel.wait_for_page_to_load("30000")
            sel.type("ctl00_ContentPlaceHolder1_FormView1_descriptionTextBox", "The conference will be held this year in New Zealand, land where J R R Tolkien's novels of heroism, bravery, ultimate quests and triumph of good over evil were portrayed on the silver screen. Much hacking will be done.")
            sel.click("//*[@id=\"ctl00_ContentPlaceHolder1_FormView1_apply1\"]")
            sel.wait_for_page_to_load("30000")
            sel.click("ctl00_TopNavRepeat_ctl01_HyperLink1")
            sel.wait_for_page_to_load("30000")
            sel.click("//*[@id=\"ctl00_ContentPlaceHolder1_lv1_logout\"]")
            sel.wait_for_page_to_load("30000")
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
