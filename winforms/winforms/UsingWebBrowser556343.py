#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_UsingWebBrowser556343Test(winformsTestCase):
    testcaseid = 556343
    command = 'UsingWebBrowser'
    message = 'Browse websites\n1. Default location is www.go-mono.com\n2. Open by clicking on Go\n3. Maker sure there are no rendering errors\nRepeat for http://slashdot.org and http://www.lwn.net\nThis test case does not work on MacOSX'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
