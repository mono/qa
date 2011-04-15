#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_CSharpTetris426254Test(winformsTestCase):
    testcaseid = 426254
    command = 'CSharpTetris'
    message = 'Play a game\nEnter - start game\nspace - drop\nz - move left\nm - move right\na - rotate left\nk - rotate right'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
