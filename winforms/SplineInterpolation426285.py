#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_SplineInterpolation426285Test(winformsTestCase):
    testcaseid = 426285
    command = 'SplineInterpolation'
    message = 'Move points'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
