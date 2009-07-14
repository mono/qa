from selenium import selenium
import unittest, time, re

class 0500_modifyProfileTest(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://change-this-to-the-site-you-are-testing/")
        self.selenium.start()
    
    def test_0500_modify_profile(self):
        sel = self.selenium
        sel.open("/blogengine/")
        sel.click("ctl00_aLogin")
        sel.wait_for_page_to_load("30000")
        sel.type("ctl00_cphBody_Login1_UserName", "admin")
        sel.type("ctl00_cphBody_Login1_Password", "admin")
        sel.click("ctl00_cphBody_Login1_LoginButton")
        sel.wait_for_page_to_load("30000")
        sel.click("//ul[@id='ctl00_42fcbe7c2c9c440abad965a94472fccc_uxMenu_ulMenu']/li[8]/a/span")
        sel.wait_for_page_to_load("30000")
        sel.select("ctl00_cphAdmin_ddlUserList", "label=mono user")
        sel.click("ctl00_cphAdmin_lbChangeUserProfile")
        sel.wait_for_page_to_load("30000")
        sel.type("ctl00_cphAdmin_tbDisplayName", "Mono User")
        sel.type("ctl00_cphAdmin_tbFirstName", "Rupert")
        sel.type("ctl00_cphAdmin_tbMiddleName", "The")
        sel.type("ctl00_cphAdmin_tbLastName", "Monkey")
        sel.type("ctl00_cphAdmin_tbEmailAddress", "mono@example.com")
        sel.type("ctl00_cphAdmin_tbCityTown", "Provo")
        sel.type("ctl00_cphAdmin_tbRegionState", "Utah")
        sel.type("ctl00_cphAdmin_tbCompany", "Novell")
        sel.click("//a[@id='ctl00_cphAdmin_tbAboutMe_TinyMCE1_txtContent_code']/span")
        for i in range(60):
            try:
                if sel.is_element_present("htmlSource"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type("htmlSource", "I am a Code Monkey")
        sel.click("insert")
        sel.click("ctl00_cphAdmin_lbSaveProfile")
        sel.wait_for_page_to_load("30000")
        sel.click("link=Logout")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
