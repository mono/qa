#!/usr/bin/env python

import sys
import os
import unittest
import uuid

basepath = os.path.dirname(os.path.realpath(__file__))
while not os.path.isfile(os.path.join(basepath,'common','monoTestCase.py')):
    basepath = os.path.dirname(basepath)
if not basepath in sys.path:
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
