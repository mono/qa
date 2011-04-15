#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_Monodoc429868Test(winformsTestCase):
    testcaseid = 429868
    command = 'monodoc'
    message = 'Look for Console.WriteLine in the index tab'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
