#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.apache.apacheTestCase import apacheTestCase

class be_1100_ChangeUserProfileAsMonoUserTest(apacheTestCase):
    apacheTestCaseId = 875598
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
            sel.click("//ul[@id='ctl00_42fcbe7c2c9c440abad965a94472fccc_uxMenu_ulMenu']/li[6]/a/span")
            sel.wait_for_page_to_load("30000")
            sel.type("ctl00_cphAdmin_tbDisplayName", "Mono User")
            sel.type("ctl00_cphAdmin_tbFirstName", "Mono")
            sel.type("ctl00_cphAdmin_tbFirstName", "Rupert")
            sel.type("ctl00_cphAdmin_tbMiddleName", "The")
            sel.type("ctl00_cphAdmin_tbLastName", "Monkey")
            sel.type("ctl00_cphAdmin_tbPhoneMain", "801.555.1234")
            sel.type("ctl00_cphAdmin_tbEmailAddress", "mono@example.com")
            sel.type("ctl00_cphAdmin_tbCityTown", "Provo")
            sel.type("ctl00_cphAdmin_tbRegionState", "Utah")
            sel.type("ctl00_cphAdmin_tbCompany", "Novell Inc.")
            sel.click("//a[@id='ctl00_cphAdmin_tbAboutMe_TinyMCE1_txtContent_code']/span")
            for i in range(60):
                try:
                    if sel.is_element_present("htmlSource"): break
                except: pass
                time.sleep(1)
            else: self.fail("time out")
            sel.type("htmlSource", "<p>\nPhasellus volutpat elementum odio, vitae lobortis enim tincidunt nec! Nullam sit amet leo sit amet erat cursus elementum. Donec placerat blandit orci; id placerat enim posuere eget. Curabitur gravida gravida lorem vitae accumsan. Nulla blandit urna ut felis scelerisque gravida. Phasellus malesuada auctor ante vel vehicula. Sed consequat libero ut erat dictum ut dapibus turpis mattis. Integer vitae leo at ipsum pellentesque malesuada. Praesent ut nunc metus. Proin a dui nisi. Donec eu augue eu augue mollis ultrices. Mauris facilisis, nisi nec tempus consequat; nisi tellus commodo metus, eget tristique urna mauris quis quam. Sed dictum pretium ultrices.\n</p>\n\n<p>\nCurabitur lacus lacus, egestas nec vestibulum id, accumsan vel est. Fusce ac sapien enim. Donec sollicitudin malesuada placerat? Duis convallis consequat quam. Sed lacus erat, laoreet nec imperdiet ornare, eleifend sit amet mi! Pellentesque ultrices pellentesque orci, nec tincidunt sem cursus sit amet. Ut pellentesque mi eu nisl bibendum aliquet. Phasellus molestie, mi sed iaculis molestie; justo velit dapibus tortor, at commodo dolor elit ac velit. Phasellus eu blandit massa. Donec in lacus urna. Phasellus congue facilisis cursus. Phasellus eget ligula nulla, a molestie sem.\n</p>\n\n<p>\nSuspendisse potenti. In sed orci eget velit eleifend tincidunt ac vitae libero. Phasellus sodales accumsan congue. Sed accumsan lorem ac felis aliquam imperdiet. Etiam leo est, mattis facilisis faucibus in; ullamcorper sed nulla. Cras orci ante, commodo in facilisis sed, fringilla at eros. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus sed nunc mollis felis porta tristique. Aliquam erat volutpat. Donec faucibus, odio sit amet lobortis posuere, lacus dui vulputate arcu, posuere ultricies lacus libero at eros? Maecenas sagittis ultricies pretium. Morbi ullamcorper nisi est, eu lacinia tellus? Donec facilisis erat vitae purus lacinia quis dictum lectus vulputate.\n</p>")
            sel.click("insert")
            sel.click("ctl00_cphAdmin_lbSaveProfile")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Go to front page")
            sel.wait_for_page_to_load("30000")

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
