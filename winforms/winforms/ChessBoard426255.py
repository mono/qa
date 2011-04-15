#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_ChessBoard426255Test(winformsTestCase):
    testcaseid = 426255
    command = 'ChessBoard'
    message = 'Make a valid move'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
