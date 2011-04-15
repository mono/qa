#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_NPlot426268Test(winformsTestCase):
    testcaseid = 426268
    command = 'NPlot'
    message = 'Run the Muti-Plot Demo'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
