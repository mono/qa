#!/usr/bin/env python


import sys
sys.path.append('../../..')
from selenium.selenium import selenium
from selenium.seleniumTestCase import *
from common.monotesting import *

import unittest, time, re

class AspNetFramework_session1(seleniumTestCase):
    testcaseid = 838727

    def test(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=session1")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("You can write here.", sel.get_text("txt1"))
        sel.type("txt1", "This is new text.")
        sel.click("btn")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_text_present("Somebody pressed me"))
        self.failUnless(sel.is_text_present("Text have changed"))
        sel.click("btn")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_text_present("Somebody pressed me"))
        sel.type("txt1", "This is more new text.")
        sel.click("btn")
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_text_present("Somebody pressed me"))
        self.failUnless(sel.is_text_present("Text have changed"))
        self.failUnless(sel.is_text_present("This is more new text."))

if __name__ == "__main__":
    monotesting_main()


# vim:ts=4:expandtab:
