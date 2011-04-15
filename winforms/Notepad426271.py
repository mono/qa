#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_Notepad426271Test(winformsTestCase):
    testcaseid = 426271
    command = 'Notepad'
    message = 'Enter some text\nChange the text font size to 24'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
