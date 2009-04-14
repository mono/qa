#!/usr/bin/env python

import sys
sys.path.append('../../../..')
import common.monotesting as mono
from selenium.xsp1 import xsp1TestCase

import unittest, time, re

class WebService_TestService_EchoTest(xsp1TestCase.xsp1TestCase):
    def __init__(self,methodname='test_new'):
        xsp1TestCase.xsp1TestCase.__init__(self,methodname)
        if not mono.usexsp2:
            self.testcaseid = 426296
        else:
            self.testcaseid = 841152


    def test_new(self):
        print "derived class.test()"
        if not self.canRun:
            return
        try: 
            sel = self.selenium
            sel.open("/index.aspx")
            sel.click("link=TestService.asmx")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Echo")
            sel.wait_for_page_to_load("30000")
            sel.click("//a[2]/span")
            sel.wait_for_page_to_load("30000")
            sel.type("a", "this is a test")
            sel.click("//input[@value='Invoke']")
            sel.wait_for_page_to_load("30000")
            self.failUnless(re.search(r"^[\s\S]*this is a test[\s\S]*$", sel.get_text("//html/body/table/tbody/tr/td[2]/div/div/div")))

        except Exception, e:
            self.verificationErrors.append(str(e))
    

if __name__ == "__main__":
    mono.monotesting_main()




# vim:ts=4:expandtab:
