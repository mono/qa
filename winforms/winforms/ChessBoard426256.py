#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_ChessBoard426256Test(winformsTestCase):
    testcaseid = 426256
    command = 'ChessBoard'
    message = 'Make an invalid move'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
