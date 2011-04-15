#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_SVGPad426279Test(winformsTestCase):
    testcaseid = 426279
    command = 'SVGPad'
    message = 'Create Document'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
