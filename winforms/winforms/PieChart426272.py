#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_PieChart426272Test(winformsTestCase):
    testcaseid = 426272
    command = 'PieChart'
    message = 'Increase the value of a pie slice'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
