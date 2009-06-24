#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../..')
import common.monotesting as mono
from selenium.graffiti.graffitiTestCase import graffitiTestCase
import re

class graffiti_ee_deletePosts(graffitiTestCase):
    graffitiTestCaseId = None
    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=Login")
            sel.wait_for_page_to_load("30000")
            sel.type("UserName", "admin")
            sel.type("Password", "mono")
            sel.click("login")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Posts")
            sel.wait_for_page_to_load("30000")

##################################
            # Find index for first story, build XPath with it, delete
            href = sel.get_attribute("link=Cras tristique, enim ac ornare facilisis, ante justo euismod urna; ac varius nisl libero sed velit?@href")
            match = re.match(r'.*=(.*)',href)
            print("Deleting first story: " + match.group(1))
            sel.click('//*[@id="post-' + match.group(1) + '"]/td[4]/a[2]')

##################################

            # Find index for second story, build XPath, delete
            href = sel.get_attribute("link=Pellentesque tempus mollis pharetra. Etiam blandit risus augue, eget venenatis elit?@href")
            match = re.match(r'.*=(.*)',href)
            print("Deleting second story: " + match.group(1))
            sel.click('//*[@id="post-' + match.group(1) + '"]/td[4]/a[2]')
            

####################################
            # Confirm stories are gone

            for i in range(60):
                try:
                    if sel.is_element_present("//html/body/div/div/div[4]/ul/li[3]/a"): break
                except: pass
                time.sleep(1)
            else: self.fail("time out")
            sel.click("//html/body/div/div/div[4]/ul/li[3]/a")
            sel.wait_for_page_to_load("30000")
            self.failIf(sel.is_text_present("link=Cras tristique, enim ac ornare facilisis, ante justo euismod urna; ac varius nisl libero sed velit?"))
            self.failIf(sel.is_text_present("link=Pellentesque tempus mollis pharetra. Etiam blandit risus augue, eget venenatis elit?"))

            sel.click("link=Log Off")
            sel.wait_for_page_to_load("30000")
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
