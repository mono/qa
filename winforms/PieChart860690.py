#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_PieChart860690Test(winformsTestCase):
    testcaseid = 860690
    command = 'PieChart'
    message = 'Print the pie chart to a file\n1. In the print dialog, make sure to check the "To file" check box.\n2. Open the file by typing gnome-open <filename>\nThe chart should be printed to file and it should be able to be opened by gnome-open'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
