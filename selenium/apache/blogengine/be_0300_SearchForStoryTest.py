#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.apache.apacheTestCase import apacheTestCase

class be_0300_SearchForStoryTest(apacheTestCase):
    apacheTestCaseId = 875590
    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/blogengine/")
            sel.click("link=Home")
            sel.wait_for_page_to_load("30000")
            sel.type("searchfield", "mono story")
            sel.click("searchbutton")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("This is a story about Mono. Lorem ipsum dolor sit amet, consectetur adipiscing elit"))
            sel.click("link=Mono Story")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("This is a story about Mono. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus non hendrerit turpis. Pellentesque quis lectus scelerisque augue semper dignissim id a est. Etiam dignissim; sem et aliquam sollicitudin, nisl tellus gravida urna, in elementum ligula elit vel mi. Maecenas viverra felis ac urna volutpat rutrum. Etiam vestibulum fringilla porttitor. Etiam volutpat tortor ut neque pretium luctus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Cras at ipsum et enim vehicula dapibus! Fusce auctor interdum magna in molestie. Maecenas ac massa ac ligula convallis vehicula vitae id sem. Sed posuere commodo elit at rutrum. Cras mattis pharetra enim. Nulla facilisi. Nunc fermentum, nulla et hendrerit vulputate, justo ipsum luctus arcu, sit amet rhoncus turpis mauris sed erat!"))

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:

