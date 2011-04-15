#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_Monodoc429867Test(winformsTestCase):
    testcaseid = 429867
    command = 'Monodoc'
    message = 'Generate the indexes using the index tab'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
