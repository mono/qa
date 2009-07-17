#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.apache.apacheTestCase import apacheTestCase

class be_0200_CreateSoryTest(apacheTestCase):
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
            sel.click("//html/body/form/div[3]/div/div[2]/div/ul/li/a/span")
            sel.wait_for_page_to_load("30000")
            sel.type("ctl00_cphAdmin_txtTitle", "Mono Story")
            if not sel.is_checked("ctl00_cphAdmin_cbUseRaw"):
                sel.click("ctl00_cphAdmin_cbUseRaw")
                sel.wait_for_page_to_load("30000")
            sel.type("ctl00_cphAdmin_txtRawContent", '''<p>
This is a story about Mono. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus non hendrerit turpis. Pellentesque quis lectus scelerisque augue semper dignissim id a est. Etiam dignissim; sem et aliquam sollicitudin, nisl tellus gravida urna, in elementum ligula elit vel mi. Maecenas viverra felis ac urna volutpat rutrum. Etiam vestibulum fringilla porttitor. Etiam volutpat tortor ut neque pretium luctus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Cras at ipsum et enim vehicula dapibus! Fusce auctor interdum magna in molestie. Maecenas ac massa ac ligula convallis vehicula vitae id sem. Sed posuere commodo elit at rutrum. Cras mattis pharetra enim. Nulla facilisi. Nunc fermentum, nulla et hendrerit vulputate, justo ipsum luctus arcu, sit amet rhoncus turpis mauris sed erat!
</p>''')
            sel.click("ctl00_cphAdmin_btnSave")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Home")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("Mono Story"))
            sel.click("link=Mono Story")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present('''This is a story about Mono. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus non hendrerit turpis. Pellentesque quis lectus scelerisque augue semper dignissim id a est. Etiam dignissim; sem et aliquam sollicitudin, nisl tellus gravida urna, in elementum ligula elit vel mi. Maecenas viverra felis ac urna volutpat rutrum. Etiam vestibulum fringilla porttitor. Etiam volutpat tortor ut neque pretium luctus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Cras at ipsum et enim vehicula dapibus! Fusce auctor interdum magna in molestie. Maecenas ac massa ac ligula convallis vehicula vitae id sem. Sed posuere commodo elit at rutrum. Cras mattis pharetra enim. Nulla facilisi. Nunc fermentum, nulla et hendrerit vulputate, justo ipsum luctus arcu, sit amet rhoncus turpis mauris sed erat!'''))
            sel.click("link=5")
            self.assertEqual("Your rating has been registered. Thank you!", sel.get_alert())
            sel.click("ctl00_aLogin")
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
