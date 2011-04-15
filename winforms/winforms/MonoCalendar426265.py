#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_MonoCalendar426265Test(winformsTestCase):
    testcaseid = 426265
    command = 'MonoCalendar'
    message = 'Delete an appointment'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
