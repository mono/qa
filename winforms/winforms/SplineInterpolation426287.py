#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_SplineInterpolation426287Test(winformsTestCase):
    testcaseid = 426287
    command = 'SplineInterpolation'
    message = 'Clear all points'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
