#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_PolygonTriangulation426276Test(winformsTestCase):
    testcaseid = 426276
    command = 'PolygonTriangulation'
    message = 'Cut the ear using mouse clicks'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
