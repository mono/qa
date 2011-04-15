#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_PieChart860688Test(winformsTestCase):
    testcaseid = 860688
    command = 'PieChart'
    message = 'Print the pie chart to the default printer'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
