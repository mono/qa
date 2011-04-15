#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_PolygonTriangulation426275Test(winformsTestCase):
    testcaseid = 426275
    command = 'PolygonTriangulation'
    message = 'Clean the screen'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
