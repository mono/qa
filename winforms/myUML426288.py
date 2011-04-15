#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_myUML426288Test(winformsTestCase):
    testcaseid = 426288
    command = 'myUML'
    message = 'Create a use case'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
