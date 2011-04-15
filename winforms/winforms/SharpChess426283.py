#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_SharpChess426283Test(winformsTestCase):
    testcaseid = 426283
    command = 'SharpChess'
    message = 'Play a game against the computer'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
