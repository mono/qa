#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_ReportBuilder426277Test(winformsTestCase):
    testcaseid = 426277
    command = 'ReportBuilder'
    message = 'Sort by the Order ID columnt'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
