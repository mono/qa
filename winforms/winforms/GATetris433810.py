#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_GATetris433810Test(winformsTestCase):
    testcaseid = 433810
    command = 'GATetris'
    message = 'Change key bindings\nClick Options / Settings\nIn the keyboard section, change the PauseKey to "Q"\nClick Ok\nStart a game and press Q to make sure it pauses'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
