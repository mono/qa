#!/usr/bin/python

import sys,os
import unittest
import traceback
import subprocess
import uuid

filepath = os.path.realpath(__file__)
basepath = os.path.dirname(os.path.dirname(filepath))
#basepath is the absolute path of the trunk/qa directory

sys.path.append(basepath)
import common.monotesting as mono
from smokeTestCase import smokeTestCase
from common.helpers import *


####################################################################
#
#    xsp1TestCase class
#

class gacutilTestCase(smokeTestCase):
    testcaseid = 0

    def test(self):

        out = executeCmd('gacutil -l System')
        self.assert_(out[1].find('b77a5c561934e089') > 0)

if __name__ == '__main__':
    mono.monotesting_main()



# vim:ts=4:expandtab:
