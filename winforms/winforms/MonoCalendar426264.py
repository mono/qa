#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_MonoCalendar426264Test(winformsTestCase):
    testcaseid = 426264
    command = 'MonoCalendar'
    message = 'Move an appointment to another day'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
