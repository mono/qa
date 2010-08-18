#!/usr/bin/env python

import sys, unittest, time, re
import os

basepath = os.path.dirname(os.path.realpath(__file__))
while not os.path.isfile(os.path.join(basepath,'common','monoTestCase.py')):
    basepath = os.path.dirname(basepath)
if not basepath in sys.path:
    sys.path.append(basepath)

import common.monotesting as mono
from selenium.xsp4.xsp4TestCase import xsp4TestCase


class menu_menu1Test(xsp4TestCase):
    testcaseid = 863925

    def _isMenuNormal(self, jsLocator):
        className = self.selenium.get_eval("this.browserbot.findElement(" + jsLocator + ").className;")
        return (className == "Menu1_1")

    def _isMenuHovered(self, jsLocator):
        className = self.selenium.get_eval("this.browserbot.findElement(" + jsLocator + ").className;")
        return (className == "Menu1_1 Menu1_9")

    def _isMenuItemNormal(self, jsLocator):
        className = self.selenium.get_eval("this.browserbot.findElement(" + jsLocator + ").className;")
        return (className == "Menu1_1 Menu1_4")

    def _isMenuItemHovered(self, jsLocator):
        className = self.selenium.get_eval("this.browserbot.findElement(" + jsLocator + ").className;")
        return (className == "Menu1_1 Menu1_4 Menu1_11")

    def _isMenuItemSelected(self, jsLocator):
        className = self.selenium.get_eval("this.browserbot.findElement(" + jsLocator + ").className;")
        return (className == "Menu1_1 Menu1_4 Menu1_7")

    def _hoverMenuTest(self, jsLocator):
        sel = self.selenium
        locatorXPath = "//*[@" + jsLocator + "]"
        self.failUnless(self._isMenuNormal(jsLocator))
        sel.mouse_over(locatorXPath)
        self.failUnless(self._isMenuHovered(jsLocator))
        sel.mouse_out(locatorXPath)
        self.failIf(self._isMenuHovered(jsLocator))
        sel.click(locatorXPath)
        sel.wait_for_page_to_load("30000")
        self.failIf(self._isMenuHovered(jsLocator))

    def _hoverSelectMenuItemTest(self, jsLocator):
        sel = self.selenium
        locatorXPath = "//*[@" + jsLocator + "]"
        self.failUnless(self._isMenuItemNormal(jsLocator))
        sel.mouse_over(locatorXPath)
        self.failUnless(self._isMenuItemHovered(jsLocator))
        sel.click(locatorXPath)
        sel.wait_for_page_to_load("30000")
        self.failUnless(self._isMenuItemSelected(jsLocator))

    def test(self):
        try:
            # These are the main menus
            menus = { "PartI":"id=\"Menu1_0l\"",
                      "PartII":"id=\"Menu1_1l\"",
                      "PartIII":"id=\"Menu1_2l\"" }

            # These are the sub-menu items
            menuItems = { "partIChapter1":"id=\"Menu1_0_0l\"",
                          "partIChapter2":"id=\"Menu1_0_1l\"",
                          "partIChapter3":"id=\"Menu1_0_2l\"",
                          "partIChapter31":"id=\"Menu1_0_2_0l\"",
                          "partIChapter32":"id=\"Menu1_0_2_1l\"",
                          "partIChapter33":"id=\"Menu1_0_2_2l\"",
                          "partIChapter331":"id=\"Menu1_0_2_2_0l\"",
                          "partIChapter332":"id=\"Menu1_0_2_2_1l\"",
                          "partIIChapter5":"id=\"Menu1_1_0l\"",
                          "partIIChapter6":"id=\"Menu1_1_1l\"" }

            # Add the Edit/A large one/Option sub-menu items
            #for ix in range(0, 60):
            #    menuItems["option" + str(ix+1)] = "id=\"Menu12_1_5_" + str(ix) + "l\""

            # Finally start testing
            print "Starting Selenium"
            sel = self.selenium
            sel.open("/")
            sel.click("//*[@id=\"TreeView2_0_0_0_img\"]")
            sel.click("//*[@id=\"TreeView2_0_0_0_1_txt\"]")
            sel.wait_for_page_to_load("30000")

            # Test the upper menus (file and edit)
            for menu in menus:
                self._hoverMenuTest(menus[menu])

            # Test the sub-menu items (new, cut, etc)
            for menuItem in menuItems:
                self._hoverSelectMenuItemTest(menuItems[menuItem])

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
