# vim:ts=4:expandtab:
import sys,os
import unittest
import traceback

filepath = os.path.realpath(__file__)
basepath = os.path.dirname(os.path.dirname(os.path.dirname(filepath)))
#basepath is the absolute path of the trunk/qa directory

sys.path.append(basepath)

import common.monotesting as mono
from common.monotesting import log
from common.monoTestCase import monoTestCase
from selenium.seleniumTestCase import seleniumTestCase

log("sys.path = %s" % (str(sys.path)))

####################################################################
#
#    xsp1TestCase class
#

class xsp2TestCase(seleniumTestCase):
    testcaseid = 0
    port = mono.xsp2_port

def monotesting_main():
    mono.monotesting_main()
