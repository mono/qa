#!/usr/bin/env python

import sys,os
import unittest
import uuid

filepath = os.path.realpath(__file__)
basepath = os.path.dirname(os.path.dirname(os.path.dirname(filepath)))
#basepath is the absolute path of the trunk/qa directory

sys.path.append(basepath)
import common.monotesting as mono
from smoketests.smokeTestCase import smokeTestCase
from common.helpers import *


####################################################################
#
#    gacutilTestCase class
#

class gacutilTestCase(smokeTestCase):
    testcaseid = 875241

    def test(self):

        out = executeCmd('gacutil -l System')
        self.assert_(out[1].find('b77a5c561934e089') > 0)

if __name__ == '__main__':
    mono.monotesting_main()



# vim:ts=4:expandtab:
