#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.apache.apacheTestCase import apacheTestCase

class be_0800_createStoryAsMonoUserTestt(apacheTestCase):
    apacheTestCaseId = None
    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/blogengine/")
            sel.click("ctl00_aLogin")
            sel.wait_for_page_to_load("30000")
            sel.type("ctl00_cphBody_Login1_UserName", "mono user")
            sel.type("ctl00_cphBody_Login1_Password", "mono")
            sel.click("ctl00_cphBody_Login1_LoginButton")
            sel.wait_for_page_to_load("30000")
            sel.click("//html/body/form/div[3]/div/div[2]/div/ul/li/a/span")
            sel.wait_for_page_to_load("30000")
            sel.type("ctl00_cphAdmin_txtTitle", "Mono Story 2")
            if not sel.is_checked("ctl00_cphAdmin_cbUseRaw"):
                sel.click("ctl00_cphAdmin_cbUseRaw")
                sel.wait_for_page_to_load("30000")
            sel.type("ctl00_cphAdmin_txtRawContent", "<p>This is a story by mono user<p>")
            sel.type("ctl00_cphAdmin_txtRawContent", "<p>This is a story by mono user<p>\n<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer molestie justo a augue facilisis interdum. Sed sollicitudin lobortis dapibus. Suspendisse vitae urna urna, et posuere turpis! Nulla sed erat dui, eget interdum odio. Nullam id tortor et elit volutpat vulputate ac sit amet odio. Proin nisl est, pretium non dapibus id, vestibulum sed orci. Mauris lobortis diam eu mi pulvinar ut vehicula velit convallis. Quisque malesuada porttitor ante ut porta! Nunc magna ipsum, lobortis vitae luctus eu, varius et quam! Sed non metus imperdiet massa aliquam tristique sit amet auctor lacus. Maecenas sollicitudin varius aliquet. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin non ipsum metus, vel elementum quam! Sed interdum metus pharetra elit accumsan sit amet semper purus auctor. Nunc eget dolor ac nibh molestie iaculis in at mi. Nunc velit nisl, venenatis at tempus id, adipiscing et ligula. Aliquam erat volutpat. Mauris eget commodo erat.</p>")
            cat_check_xpath = "//span[@id='ctl00_cphAdmin_cblCategories']/label[text()='Mono']/preceding-sibling::input[1]"
            if sel.is_element_present(cat_check_xpath) and not sel.is_checked(cat_check_xpath):
                sel.click(cat_check_xpath)
            else:
                mono.log("No category 'Mono' exists.  Not setting a catagory.")
            sel.click("ctl00_cphAdmin_btnSave")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Home")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Mono Story 2")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("This is a story by mono user"))
            self.failUnless(sel.is_text_present("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer molestie justo a augue facilisis interdum. Sed sollicitudin lobortis dapibus. Suspendisse vitae urna urna, et posuere turpis! Nulla sed erat dui, eget interdum odio. Nullam id tortor et elit volutpat vulputate ac sit amet odio. Proin nisl est, pretium non dapibus id, vestibulum sed orci. Mauris lobortis diam eu mi pulvinar ut vehicula velit convallis. Quisque malesuada porttitor ante ut porta! Nunc magna ipsum, lobortis vitae luctus eu, varius et quam! Sed non metus imperdiet massa aliquam tristique sit amet auctor lacus. Maecenas sollicitudin varius aliquet. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin non ipsum metus, vel elementum quam! Sed interdum metus pharetra elit accumsan sit amet semper purus auctor. Nunc eget dolor ac nibh molestie iaculis in at mi. Nunc velit nisl, venenatis at tempus id, adipiscing et ligula. Aliquam erat volutpat. Mauris eget commodo erat."))
            sel.click("ctl00_aLogin")

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
