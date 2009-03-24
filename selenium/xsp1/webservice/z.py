#!/usr/bin/env python

import sys
import time, re

sys.path.append('../..')
from selenium import selenium
from unittest import *
from monotesting import *

verificationErrors = []
sel = None

def setUp():
        global verifcationErrors
        global sel
        verificationErrors = []
        sel = selenium(rc_server, rc_port, rc_browser, rc_host)
        sel.start()
    
def main():

        global sel
        global verificationErrors

        setUp()

        sel.open("/index.aspx")
        sel.click("link=TestService.asmx")
        sel.wait_for_page_to_load("30000")
        sel.click("link=Add")
        sel.wait_for_page_to_load("30000")
        sel.click("//a[2]/span")
        sel.wait_for_page_to_load("30000")
        sel.type("a", "5238")
        sel.type("b", "8361")
        sel.click("//input[@value='Invoke']")
        sel.wait_for_page_to_load("30000")
        #try: TestCase().failUnless(re.search(r"^[\s\S]*13599[\s\S]*$", sel.get_text("//html/body/table/tbody/tr/td[2]/div/div/div")))
        #except AssertionError, e: TestCase.verificationErrors.append(str(e))

        tearDown()
    
def tearDown():
        
        sel.stop()
        #TestCase().assertEqual([], verificationErrors)

    

if __name__ == "__main__":
    main()
