#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_MoMA496504Test(winformsTestCase):
    testcaseid = 496504
    command = 'moma'
    message = 'Submit a MoMA report\n1. Add Assembly by selecting /mnt/mtester/tests/manual/moma/PaintDotNet.exe, Click Open then Next  (PolygonTriangulation can work too)\n2. Note errors, click View Detail Report. This will open up Firefox with the report.\n3. Close Firefox, click Next\n4. Fill in fields. use qa@novell.com for email address. Other field content can be random.\n5. Click Submit Report, note results, then click Close.'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
