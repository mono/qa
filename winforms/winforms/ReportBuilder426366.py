#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_ReportBuilder426366Test(winformsTestCase):
    testcaseid = 426366
    command = 'ReportBuilder'
    message = 'Edit a cell'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
