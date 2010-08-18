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


class Treeview_PopulateOnDemand(xsp4TestCase):
    testcaseid = 865599
    __numFaults = 0
    __maxTimeToPause = 0.100


    def __waitForNodeToExpand(self, jsLocator):
        ix = 0
        max = 10
        while ix < max and self.__isCollapsed(jsLocator):
            ix += 1
            time.sleep(self.__maxTimeToPause / max)
        if ix == max:
            raise Exception("Took too long to expand node [" + jsLocator + "]")

    def __getStyle(self, jsLocator):
        style = self.selenium.get_eval("this.browserbot.findElement(\"" + jsLocator + "\").getAttribute(\"style\");")
        return style

    def __isExpanded(self, jsLocator):
        return (self.__getStyle(jsLocator) == "display: block;")

    def __isCollapsed(self, jsLocator):
        return (self.__getStyle(jsLocator) == "display: none;")

    def __getAlt(self, jsLocator):
        alt = self.selenium.get_eval("this.browserbot.findElement(\"" + jsLocator + "\").getAttribute(\"alt\");")
        return alt

    def __isLeafEmpty(self, jsLocator):
        if re.search(r"^Expand Node.*", self.__getAlt(jsLocator)):
            return True
        else:
            return False

    def __isLeafExpanded(self, jsLocator):
        return (self.__getAlt(jsLocator) == "Collapse ")

    def __isLeafCollapsed(self, jsLocator):
        return (self.__getAlt(jsLocator) == "Expand ")

    def __expandAndCheck(self, jsLocator):
        self.failUnless(self.__isCollapsed(jsLocator))
        self.selenium.click(jsLocator + "_img")
        self.__waitForNodeToExpand(jsLocator)

    def __expandLastLeafAndCheck(self, jsLocator):
        self.failUnless(self.__isLeafEmpty(jsLocator))
        self.selenium.click(jsLocator)
        self.failUnless(self.__isLeafEmpty(jsLocator))
        self.selenium.click(jsLocator)
        self.failUnless(self.__isLeafExpanded(jsLocator))
        self.selenium.click(jsLocator)
        self.failUnless(self.__isLeafCollapsed(jsLocator))

    def __collapseAndCheck(self, jsLocator):
        self.failUnless(self.__isExpanded(jsLocator))
        self.selenium.click(jsLocator + "_img")
        self.failUnless(self.__isCollapsed(jsLocator))

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("//*[@id=\"TreeView2_0_0_3_img\"]")
            sel.click("//*[@id=\"TreeView2_0_0_3_1_txt\"]")
            sel.wait_for_page_to_load("30000")

            baseJsLocator = "id=TreeView1"
            for ix in range(1):
                # Inventory
                self.__expandAndCheck(baseJsLocator + "_" + str(ix))
                for ix2 in range(2):
                    # Node0
                    self.__expandAndCheck(baseJsLocator + "_" + str(ix) + "_" + str(ix2))
                    for ix3 in range(4):
                        # Node0A
                        self.__expandAndCheck(baseJsLocator + "_" + str(ix) + "_" + str(ix2) + "_" + str(ix3))
                        for ix4 in range(6):
                            # Node0A0
                            self.__expandAndCheck(baseJsLocator + "_" + str(ix) + "_" + str(ix2) + "_" + str(ix3) + "_" + str(ix4))
                            for ix5 in range(8):
                                # Node0A0A
                                self.__expandAndCheck(baseJsLocator + "_" + str(ix) + "_" + str(ix2) + "_" + str(ix3) + "_" + str(ix4) + "_" + str(ix5))
                                # This last layer just makes the test take too long.
                                # It works if you uncomment it
                                #for ix6 in range(10):
                                #   # Node0A0A0
                                #   self.__expandLastLeafAndCheck(baseJsLocator + "_" + str(ix) + "_" + str(ix2) + "_" + str(ix3) + "_" + str(ix4) + "_" + str(ix5) + "_" + str(ix6) + "_img")
                                self.__collapseAndCheck(baseJsLocator + "_" + str(ix) + "_" + str(ix2) + "_" + str(ix3) + "_" + str(ix4) + "_" + str(ix5))
                            self.__collapseAndCheck(baseJsLocator + "_" + str(ix) + "_" + str(ix2) + "_" + str(ix3) + "_" + str(ix4))
                        self.__collapseAndCheck(baseJsLocator + "_" + str(ix) + "_" + str(ix2) + "_" + str(ix3))
                    self.__collapseAndCheck(baseJsLocator + "_" + str(ix) + "_" + str(ix2))
                self.__collapseAndCheck(baseJsLocator + "_" + str(ix))


        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
