from selenium import selenium
import unittest, time, re

class 0400_createUserTest(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://change-this-to-the-site-you-are-testing/")
        self.selenium.start()
    
    def test_0400_create_user(self):
        sel = self.selenium
        sel.open("/blogengine/")
        sel.click("ctl00_aLogin")
        sel.wait_for_page_to_load("30000")
        sel.type("ctl00_cphBody_Login1_UserName", "admin")
        sel.type("ctl00_cphBody_Login1_Password", "admin")
        sel.click("ctl00_cphBody_Login1_LoginButton")
        sel.wait_for_page_to_load("30000")
        sel.click("//ul[@id='ctl00_42fcbe7c2c9c440abad965a94472fccc_uxMenu_ulMenu']/li[9]/a/span")
        sel.wait_for_page_to_load("30000")
        sel.type("ctl00_cphAdmin_CreateUserWizard1_ctl02_UserName", "mono user")
        sel.type("ctl00_cphAdmin_CreateUserWizard1_ctl02_Password", "mono")
        sel.type("ctl00_cphAdmin_CreateUserWizard1_ctl02_ConfirmPassword", "mono")
        sel.type("ctl00_cphAdmin_CreateUserWizard1_ctl02_Email", "mono@example.com")
        sel.click("ctl00_cphAdmin_CreateUserWizard1_CustomNavContainer0_StepNextButtonButton")
        sel.wait_for_page_to_load("30000")
        sel.click("link=Logout")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
