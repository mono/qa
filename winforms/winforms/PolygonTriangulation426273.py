#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_PolygonTriangulation426273Test(winformsTestCase):
    testcaseid = 426273
    command = 'PolygonTriangulation'
    message = 'Draw a Polygon using test data'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
