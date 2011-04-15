#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_SplineInterpolation426286Test(winformsTestCase):
    testcaseid = 426286
    command = 'SplineInterpolation'
    message = 'Delete points'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
