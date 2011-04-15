#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_Rubik426278Test(winformsTestCase):
    testcaseid = 426278
    command = 'Rubik'
    message = 'Scramble then try to solve for one side'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
