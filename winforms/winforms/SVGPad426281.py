#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_SVGPad426281Test(winformsTestCase):
    testcaseid = 426281
    command = 'SVGPad'
    message = 'Save the document'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
