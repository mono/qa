#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_AnotherTetrisClone426253Test(winformsTestCase):
    testcaseid = 426253
    command = 'AnotherTetrisClone'
    message = 'Play a game\nLeft, Right arrows - move\nSpace bar - drop\nz - rotate left\nc - rotate right'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
