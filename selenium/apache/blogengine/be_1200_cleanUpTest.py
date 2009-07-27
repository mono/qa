#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.apache.apacheTestCase import apacheTestCase

class be_1200_cleanUpTest(apacheTestCase):
    apacheTestCaseId = None
    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/blogengine/")
            sel.click("ctl00_aLogin")
            sel.wait_for_page_to_load("30000")
            sel.type("ctl00_cphBody_Login1_UserName", "admin")
            sel.type("ctl00_cphBody_Login1_Password", "admin")
            sel.click("ctl00_cphBody_Login1_LoginButton")
            sel.wait_for_page_to_load("30000")
############
            mono.log("Delete Mono Story 2")
            sel.click("link=Mono Story 2")
            sel.wait_for_page_to_load("30000")
            sel.click("//html/body/form//div[3]/a[text()='Delete']")
            self.failUnless(re.search(r"^Are you sure you want to delete the post[\s\S]$", sel.get_confirmation()))
############
            mono.log("Delete Mono Story")
            for i in range(60):
                try:
                    if sel.is_element_present("link=Mono Story"): break
                except: pass
                time.sleep(1)
            else: self.fail("time out")
            sel.click("link=Mono Story")
            sel.wait_for_page_to_load("30000")
            for i in range(60):
                try:
                    if sel.is_element_present("//html/body/form//div[3]/a[text()='Delete']"): break
                except: pass
                time.sleep(1)
            else: self.fail("time out")
            sel.click("//html/body/form//div[3]/a[text()='Delete']")
            self.failUnless(re.search(r"^Are you sure you want to delete the post[\s\S]$", sel.get_confirmation()))
############
            mono.log("Delete Mono category")
            for i in range(60):
                try:
                    if sel.is_element_present("//a/span[text()='Categories']"): break
                except: pass
                time.sleep(1)
            else: self.fail("time out")
            sel.click("//a/span[text()='Categories']")
            sel.wait_for_page_to_load("30000")
            sel.click("//table[@class='category']/tbody/tr/td[normalize-space(text())='Mono']/preceding-sibling::td/a[text()='Delete']")
            sel.wait_for_page_to_load("30000")
############
            mono.log("Delete the Mono Page")
            sel.click("link=Go to front page")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Mono Page")
            sel.wait_for_page_to_load("30000")
            sel.click("//html/body/form/div[2]/div/div[2]/a[2]")
            self.failUnless(re.search(r"^Are you sure you want to delete the page[\s\S]$", sel.get_confirmation()))
############
            mono.log("Delete slashdot from blogroll")
            for i in range(60):
                try:
                    if sel.is_element_present("//a/span[text()='Blogroll']"): break
                except: pass
                time.sleep(1)
            else: self.fail("time out")
            sel.click("//a/span[text()='Blogroll']")
            sel.wait_for_page_to_load("30000")
            sel.click("//table[@id='contentTable']//table/tbody/tr/td[1]/a[text()='Slashdot']/../following-sibling::td/a[text()='Delete']")
            sel.wait_for_page_to_load("30000")
            self.failUnless(re.search(r"^Are you sure[\s\S]$", sel.get_confirmation()))
            for i in range(60):
                try:
                    # 'Go to front page' XPath
                    if sel.is_element_present("//form[@id='ctl00_form1']/table/tbody/tr/td[4]/a"): break
                except: pass
                time.sleep(1)
            else: self.fail("time out")
            sel.click("//form[@id='ctl00_form1']/table/tbody/tr/td[4]/a")
############
            mono.log("Delete the mono user")
            sel.wait_for_page_to_load("30000")
            sel.click("//a/span[text()='Users']")
            sel.wait_for_page_to_load("30000")
            sel.click("//span[text()='mono user']/../preceding-sibling::td/a[text()='Delete']")
            sel.wait_for_page_to_load("30000")
            self.failUnless(re.search(r"^Are you sure you want to delete mono user[\s\S]$", sel.get_confirmation()))
            sel.click("link=Go to front page")
            sel.wait_for_page_to_load("30000")
############
            mono.log("Change settings back")
            for i in range(60):
                try:
                    if sel.is_element_present("//a/span[text()='Settings']"): break
                except: pass
                time.sleep(1)
            sel.click("//a/span[text()='Settings']")
            sel.wait_for_page_to_load("30000")
            sel.type("ctl00_cphAdmin_txtName", "BlogEngine.NET")
            sel.type("ctl00_cphAdmin_txtDescription", "")
            sel.click("ctl00_cphAdmin_btnSave")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Go to front page")
            sel.wait_for_page_to_load("30000")

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
