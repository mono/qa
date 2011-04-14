#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_MoMA496505Test(winformsTestCase):
    testcaseid = 496505
    command = 'mv -v /usr/lib/moma/Definitions/* /tmp/;moma'
    message = 'Click Next\nClick on Check for newer version'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
