#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_Notepad426270Test(winformsTestCase):
    testcaseid = 426270
    command = 'Notepad'
    message = 'Open the test text file'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
