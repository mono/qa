#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_Monodoc429869Test(winformsTestCase):
    testcaseid = 429869
    command = 'Monodoc'
    message = 'Generate the searches using the search tab'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
