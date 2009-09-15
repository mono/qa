#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.apache.apacheTestCase import apacheTestCase

class be_1000_addPageAsMonoUserTest(apacheTestCase):
    apacheTestCaseId = 875597
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
            sel.click("//a/span[text()='Pages']")
            sel.wait_for_page_to_load("30000")
            for i in range(60):
                try:
                    if sel.is_element_present("//input[@id='ctl00_cphAdmin_txtTitle']"): break
                except: pass
                time.sleep(1)
            sel.type("//input[@id='ctl00_cphAdmin_txtTitle']", "Mono Page")
            sel.click("//a[@id='ctl00_cphAdmin_txtContent_TinyMCE1_txtContent_code']/span")
            for i in range(60):
                try:
                    if sel.is_element_present("htmlSource"): break
                except: pass
                time.sleep(1)
            else: self.fail("time out")
            sel.type("htmlSource", "<p>Aliquam nec justo nec nulla congue tempus. Aliquam eu egestas lorem. Nullam nec lectus sit amet risus tempus mattis id non eros. In orci lacus, porta a ultrices sed, hendrerit in velit. Vestibulum dignissim arcu id nibh ullamcorper accumsan? Suspendisse consectetur pretium elit nec ullamcorper. Aenean et mauris ac dui accumsan tempus vitae nec tortor. Aenean nec neque elit. Nunc pharetra; nulla eu laoreet vulputate, arcu dui mattis velit, et ultrices quam nunc a mi. Nullam tincidunt felis in purus tempus et aliquam metus dignissim? Sed ipsum velit, mollis vel pretium at, rhoncus vel neque. Maecenas euismod iaculis quam vel adipiscing. Cras laoreet consequat mi ac dapibus? Nunc condimentum accumsan velit. Duis adipiscing ultricies mi, non elementum nunc consequat ut. Sed varius tortor id arcu faucibus eget vehicula tortor dignissim. Vivamus ullamcorper, velit vitae rutrum bibendum, neque sapien dictum lorem, a luctus tellus dolor vel eros. Donec turpis lacus, hendrerit non bibendum vitae, dignissim ut ligula. Sed consectetur congue ornare? Praesent sit amet libero nec turpis consectetur scelerisque.</p>\n<p>Nam a gravida eros. Fusce eu tincidunt libero. Maecenas vel elit sit amet nunc scelerisque vehicula ut quis massa. Mauris euismod lectus a quam adipiscing congue. Sed fringilla ullamcorper nisi aliquet rhoncus. Donec tortor tortor, adipiscing eget imperdiet a, ultrices vel odio? Etiam dictum condimentum enim sed dictum. Nullam ullamcorper neque eget libero sollicitudin pulvinar? Maecenas in risus justo. Aenean sed nunc tortor. Etiam molestie, massa bibendum tristique pretium, nisl metus lacinia libero, vitae pretium mauris lectus varius elit. Aenean viverra mattis adipiscing. Curabitur a eleifend enim.</p>\n<p>In molestie leo scelerisque felis consequat rhoncus. Donec felis est, cursus at varius pretium, molestie non libero. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Duis hendrerit rutrum elit, at eleifend magna gravida et. Nulla malesuada facilisis massa, sed dignissim turpis posuere a. In ut elementum turpis? Cras viverra, metus eu ultricies lobortis, leo est congue libero, viverra pellentesque magna ante non eros! Nam faucibus erat facilisis sapien lobortis accumsan. Duis condimentum sapien ut odio volutpat ac rutrum nibh adipiscing. Aliquam ut nulla neque. Nullam vel massa eros.</p>")
            sel.click("insert")
            sel.click("ctl00_cphAdmin_btnSave")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Home")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_element_present("link=Mono Page"))
            sel.click("link=Mono Page")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("Aliquam nec justo nec nulla congue tempus. Aliquam eu egestas lorem. Nullam nec lectus sit amet risus tempus mattis id non eros. In orci lacus, porta a ultrices sed, hendrerit in velit. Vestibulum dignissim arcu id nibh ullamcorper accumsan? Suspendisse consectetur pretium elit nec ullamcorper. Aenean et mauris ac dui accumsan tempus vitae nec tortor. Aenean nec neque elit. Nunc pharetra; nulla eu laoreet vulputate, arcu dui mattis velit, et ultrices quam nunc a mi. Nullam tincidunt felis in purus tempus et aliquam metus dignissim? Sed ipsum velit, mollis vel pretium at, rhoncus vel neque. Maecenas euismod iaculis quam vel adipiscing. Cras laoreet consequat mi ac dapibus? Nunc condimentum accumsan velit. Duis adipiscing ultricies mi, non elementum nunc consequat ut. Sed varius tortor id arcu faucibus eget vehicula tortor dignissim. Vivamus ullamcorper, velit vitae rutrum bibendum, neque sapien dictum lorem, a luctus tellus dolor vel eros. Donec turpis lacus, hendrerit non bibendum vitae, dignissim ut ligula. Sed consectetur congue ornare? Praesent sit amet libero nec turpis consectetur scelerisque."))
            sel.click("ctl00_aLogin")

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
