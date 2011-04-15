#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_MonoCalendar426263Test(winformsTestCase):
    testcaseid = 426263
    command = 'MonoCalendar'
    message = 'Add an appointment'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
