#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_MonoCalendar426266Test(winformsTestCase):
    testcaseid = 426266
    command = 'MonoCalendar'
    message = 'Create a multi-day appointment'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
