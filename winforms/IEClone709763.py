#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_IEClone709763Test(winformsTestCase):
    testcaseid = 709763
    command = 'IEClone'
    message = 'Browse websites\n1. Default location is www.go-mono.com\n2. Open by clicking on Go\n3. Maker sure there are no rendering errors\nRepete for http://slashdot.org and http://www.lwn.net\nThis test case does not work on Mac OSX'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
