#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp2.xsp2TestCase import xsp2TestCase


class menu_menu2Test(xsp2TestCase):
    testcaseid = 863393

    def _isMenuNormal(self, jsLocator):
        className = self.selenium.get_eval("this.browserbot.findElement(" + jsLocator + ").className;")
        return (className == "Menu12_1 Menu12_3")

    def _isMenuHovered(self, jsLocator):
        className = self.selenium.get_eval("this.browserbot.findElement(" + jsLocator + ").className;")
        return (className == "Menu12_1 Menu12_3 Menu12_11")

    def _isMenuItemNormal(self, jsLocator):
        className = self.selenium.get_eval("this.browserbot.findElement(" + jsLocator + ").className;")
        return (className == "Menu12_1 Menu12_6")

    def _isMenuItemHovered(self, jsLocator):
        className = self.selenium.get_eval("this.browserbot.findElement(" + jsLocator + ").className;")
        return (className == "Menu12_1 Menu12_6 Menu12_13")

    def _isMenuItemSelected(self, jsLocator):
        className = self.selenium.get_eval("this.browserbot.findElement(" + jsLocator + ").className;")
        return (className == "Menu12_1 Menu12_6 Menu12_9")

    def _hoverMenuTest(self, jsLocator):
        sel = self.selenium
        locatorXPath = "//*[@" + jsLocator + "]"
        self.failUnless(self._isMenuNormal(jsLocator))
        sel.mouse_over(locatorXPath)
        self.failUnless(self._isMenuHovered(jsLocator))
        sel.mouse_out(locatorXPath)
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
        if not self.canRun:
            return
        try:
            # These are the main menus
            menus = { "file":"id=\"Menu12_0l\"",
                      "edit":"id=\"Menu12_1l\"" }

            # These are the sub-menu items
            menuItems = { "fileNew":"id=\"Menu12_0_0l\"",
                          "fileOpen":"id=\"Menu12_0_1l\"",
                          "fileClose":"id=\"Menu12_0_2l\"",
                          "editCut":"id=\"Menu12_1_0l\"",
                          "editCopy":"id=\"Menu12_1_1l\"",
                          "editPaste":"id=\"Menu12_1_2l\"",
                          "editEdit":"id=\"Menu12_1_3l\"",
                          "editEditCut":"id=\"Menu12_1_3_0l\"",
                          "editEditCopy":"id=\"Menu12_1_3_1l\"",
                          "editEditPaste":"id=\"Menu12_1_3_2l\"",
                          "editEditSelectAll":"id=\"Menu12_1_3_3l\"",
                          "editSelectAll":"id=\"Menu12_1_4l\"",
                          "editALargeOne":"id=\"Menu12_1_5l\"" }

            # Add the Edit/A large one/Option sub-menu items
            for ix in range(0, 60):
                menuItems["option" + str(ix+1)] = "id=\"Menu12_1_5_" + str(ix) + "l\""

            # Finally start testing
            sel = self.selenium
            sel.open("/")
            sel.click("//*[@id=\"TreeView2_0_0_0_img\"]")
            sel.click("//*[@id=\"TreeView2_0_0_0_0_txt\"]")
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
