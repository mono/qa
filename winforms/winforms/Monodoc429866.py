#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_Monodoc429866Test(winformsTestCase):
    testcaseid = 429866
    command = 'monodoc'
    message = 'Click the links in the right pane of the contents tab'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
