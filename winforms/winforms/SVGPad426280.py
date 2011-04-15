#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_SVGPad426280Test(winformsTestCase):
    testcaseid = 426280
    command = 'SVGPad'
    message = 'Add elements to document'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
