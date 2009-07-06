#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp2.xsp2TestCase import xsp2TestCase


class Treeview_Treeview(xsp2TestCase):
    testcaseid = 863926

    def _isExpanded(self, jsLocator):
        style = self.selenium.get_eval("this.browserbot.findElement(" + jsLocator + ").getAttribute(\"style\");")
        return (style == "display: block;")

    def _isNotExpanded(self, jsLocator):
        style = self.selenium.get_eval("this.browserbot.findElement(" + jsLocator + ").getAttribute(\"style\");")
        return (style == "display: none;")

    def _isTreeItemNormal(self, jsLocator):
        style = self.selenium.get_eval("this.browserbot.findElement(" + jsLocator + ").getAttribute(\"style\");")
        return (style == "null")

    def _isTreeItemSelected(self, jsLocator):
        style = self.selenium.get_eval("this.browserbot.findElement(" + jsLocator + ").getAttribute(\"style\");")
        return (style == "background-color: Yellow;")

    def _isTreeTopicNormal(self, jsLocator):
        style = self.selenium.get_eval("this.browserbot.findElement(" + jsLocator + ").getAttribute(\"style\");")
        return (style == "color: Red;")

    def _isTreeTopicSelected(self, jsLocator):
        style = self.selenium.get_eval("this.browserbot.findElement(" + jsLocator + ").getAttribute(\"style\");")
        return (style == "background-color: Yellow; color: Red;")

    def _selectTreeItemTest(self, jsLocator):
        sel = self.selenium
        locatorXPath = "//*[@" + jsLocator + "]"
        self.failUnless(self._isTreeItemNormal(jsLocator))
        sel.mouse_over(locatorXPath)
        self.failUnless(self._isTreeItemHovered(jsLocator))
        sel.click(locatorXPath)
        sel.wait_for_page_to_load("30000")
        self.failUnless(self._isTreeItemSelected(jsLocator))

    def _expandTreeTest(self, expTree):
        sel = self.selenium
        self.failUnless(self._isExpanded(expTree[1]))
        sel.click(expTree[2])
        self.failUnless(self._isNotExpanded(expTree[1]))
        sel.click(expTree[2])
        self.failUnless(self._isExpanded(expTree[1]))

    def _chkBxTreeTest(self, chkBxTree):
        sel = self.selenium
        self.failIf(sel.is_checked(chkBxTree[1]))
        sel.check(chkBxTree[1])
        self.failUnless(sel.is_checked(chkBxTree[1]))
        sel.uncheck(chkBxTree[1])
        self.failIf(sel.is_checked(chkBxTree[1]))

    def _slctItemTreeTest(self, slctTree):
        sel = self.selenium
        self.failUnless(self._isTreeItemNormal(slctTree[1]))
        sel.click(slctTree[2])
        sel.wait_for_page_to_load("30000")
        self.failUnless(self._isTreeItemSelected(slctTree[1]))

    def _slctTopicTreeTest(self, slctTree):
        sel = self.selenium
        self.failUnless(self._isTreeTopicNormal(slctTree[1]))
        sel.click(slctTree[2])
        sel.wait_for_page_to_load("30000")
        self.failUnless(self._isTreeTopicSelected(slctTree[1]))

    def test(self):
        if not self.canRun:
            return
        try:
            # These are the expandable tree items
            expTrees = [ ("TOC","id=\"LinksTreeView_0\"", "id=LinksTreeView_0_img"),
                         ("Chapter1","id=\"LinksTreeView_0_0\"", "id=LinksTreeView_0_0_img"),
                         # the following one acts different than clicking on the "Chapter 2" text
                         ("Chapter1Txt","id=\"LinksTreeView_0_0\"", "//*[@id=\"LinksTreeView_0_0_txt\"]"),
                         ("Chapter1_Section10","id=\"LinksTreeView_0_0_0\"", "id=LinksTreeView_0_0_0_img"),
                         ("Chapter1_Section11","id=\"LinksTreeView_0_0_1\"", "id=LinksTreeView_0_0_1_img"),
                         ("Chapter2","id=\"LinksTreeView_0_1\"", "id=LinksTreeView_0_1_img"),
                         ("Chapter2_Section20","id=\"LinksTreeView_0_1_0\"", "id=LinksTreeView_0_1_0_img")
                       ]

            # These are the check box tree items
            chkBxTrees = [ ("TOC", "//html/body/form/div[2]/table/tbody/tr/td[2]/input"),
                           ("Chapter1", "//html/body/form/div[2]/span/table/tbody/tr/td[3]/input"),
                           ("Chapter1_Section10", "//html/body/form/div[2]/span/span/table/tbody/tr/td[4]/input"),
                           ("Chapter1_Section10_Topic101", "//html/body/form/div[2]/span/span/span/table/tbody/tr/td[5]/input"),
                           ("Chapter1_Section10_Topic102", "//html/body/form/div[2]/span/span/span/table[2]/tbody/tr/td[5]/input"),
                           ("Chapter1_Section10_Topic103", "//html/body/form/div[2]/span/span/span/table[3]/tbody/tr/td[5]/input"),
                           ("Chapter1_Section11", "//html/body/form/div[2]/span/span/table[2]/tbody/tr/td[5]/input"),
                           ("Chapter1_Section11_Topic111", "//html/body/form/div[2]/span/span/span[2]/table/tbody/tr/td[5]/input"),
                           ("Chapter1_Section11_Topic112", "//html/body/form/div[2]/span/span/span[2]/table[2]/tbody/tr/td[5]/input"),
                           ("Chapter1_Section11_Topic113", "//html/body/form/div[2]/span/span/span[2]/table[3]/tbody/tr/td[5]/input"),
                           ("Chapter1_Section11_Topic114", "//html/body/form/div[2]/span/span/span[2]/table[4]/tbody/tr/td[5]/input"),
                           ("Chapter2", "//html/body/form/div[2]/span/table[2]/tbody/tr/td[3]/input"),
                           ("Chapter2_Section20", "//html/body/form/div[2]/span/span[2]/table/tbody/tr/td[4]/input"),
                           ("Chapter2_Section20_Topic201", "//html/body/form/div[2]/span/span[2]/span/table/tbody/tr/td[5]/input"),
                           ("Chapter2_Section20_Topic202", "//html/body/form/div[2]/span/span[2]/span/table[2]/tbody/tr/td[5]/input"),
                           ("AppendixA", "//html/body/form/div[2]/table[2]/tbody/tr/td[2]/input"),
                           ("AppendixB", "//html/body/form/div[2]/table[3]/tbody/tr/td[2]/input"),
                           ("AppendixC", "//html/body/form/div[2]/table[4]/tbody/tr/td[2]/input"),
                         ]


            # These are the selectable tree items (the blue ones in the tree)
            slctItemTrees = [ ("Chapter1_Section10", "\"//html/body/form/div[2]/span/span/table/tbody/tr/td[4]\"", "//*[@id=\"LinksTreeView_0_0_0_txt\"]"),
                              ("Chapter1_Section11", "\"//html/body/form/div[2]/span/span/table[2]/tbody/tr/td[5]\"", "//*[@id=\"LinksTreeView_0_0_1_txt\"]"),
                              ("Chapter2", "\"//html/body/form/div[2]/span/table[2]/tbody/tr/td[3]\"", "//*[@id=\"LinksTreeView_0_1_txt\"]"),
                              ("Chapter2_Section20", "\"//html/body/form/div[2]/span/span[2]/table/tbody/tr/td[4]\"", "//*[@id=\"LinksTreeView_0_1_0_txt\"]")
                        ]

            # These are the selectable tree topics (the red ones in the tree)
            slctTopicTrees = [ ("Chapter1_Section10_Topic101", "\"//html/body/form/div[2]/span/span/span/table/tbody/tr/td[5]\"", "//*[@id=\"LinksTreeView_0_0_0_0_txt\"]"),
                               ("Chapter1_Section10_Topic102", "\"//html/body/form/div[2]/span/span/span/table[2]/tbody/tr/td[5]\"", "//*[@id=\"LinksTreeView_0_0_0_1_txt\"]"),
                               ("Chapter1_Section10_Topic103", "\"//html/body/form/div[2]/span/span/span/table[3]/tbody/tr/td[5]\"", "//*[@id=\"LinksTreeView_0_0_0_2_txt\"]"),
                               ("Chapter1_Section11_Topic111", "\"//html/body/form/div[2]/span/span/span[2]/table/tbody/tr/td[5]\"", "//*[@id=\"LinksTreeView_0_0_1_0_txt\"]"),
                               ("Chapter1_Section11_Topic112", "\"//html/body/form/div[2]/span/span/span[2]/table[2]/tbody/tr/td[5]\"", "//*[@id=\"LinksTreeView_0_0_1_1_txt\"]"),
                               ("Chapter1_Section11_Topic113", "\"//html/body/form/div[2]/span/span/span[2]/table[3]/tbody/tr/td[5]\"", "//*[@id=\"LinksTreeView_0_0_1_2_txt\"]"),
                               ("Chapter1_Section11_Topic114", "\"//html/body/form/div[2]/span/span/span[2]/table[4]/tbody/tr/td[5]\"", "//*[@id=\"LinksTreeView_0_0_1_3_txt\"]"),
                               ("Chapter2_Section20_Topic201", "\"//html/body/form/div[2]/span/span[2]/span/table/tbody/tr/td[5]\"", "//*[@id=\"LinksTreeView_0_1_0_0_txt\"]"),
                               ("Chapter2_Section20_Topic202", "\"//html/body/form/div[2]/span/span[2]/span/table[2]/tbody/tr/td[5]\"", "//*[@id=\"LinksTreeView_0_1_0_1_txt\"]"),
                               ("AppendixA", "\"//html/body/form/div[2]/table[2]/tbody/tr/td[2]\"", "//*[@id=\"LinksTreeView_1_txt\"]"),
                               ("AppendixB", "\"//html/body/form/div[2]/table[3]/tbody/tr/td[2]\"", "//*[@id=\"LinksTreeView_2_txt\"]"),
                               ("AppendixC", "\"//html/body/form/div[2]/table[4]/tbody/tr/td[2]\"", "//*[@id=\"LinksTreeView_3_txt\"]"),
                             ]


            # Finally start testing
            sel = self.selenium
            sel.open("/")
            sel.click("//*[@id=\"TreeView2_0_0_3_img\"]")
            sel.click("//*[@id=\"TreeView2_0_0_3_0_txt\"]")
            sel.wait_for_page_to_load("30000")

            # Test the expandable menus
            for expTree in expTrees:
                self._expandTreeTest(expTree)

            # Test the check box menu items
            for chkBxTree in chkBxTrees:
                self._chkBxTreeTest(chkBxTree)

            # Test clicking on the tree items
            for slctItemTree in slctItemTrees:
                self._slctItemTreeTest(slctItemTree)

            # Test clicking on the tree topics
            for slctTopicTree in slctTopicTrees:
                self._slctTopicTreeTest(slctTopicTree)

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
