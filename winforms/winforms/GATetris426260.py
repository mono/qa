#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_GATetris426260Test(winformsTestCase):
    testcaseid = 426260
    command = 'GATetris'
    message = 'Play a game\nLeft Arrow - left\nRight Arrow - right\nDown Arrow - down\nUp Arrow - rotate'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
