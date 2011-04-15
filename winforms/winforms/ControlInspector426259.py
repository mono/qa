#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_ControlInspector426259Test(winformsTestCase):
    testcaseid = 426259
    command = 'ControlInspector'
    message = 'Inspect the SWF.Button control\n1. Click on the File / Windows Forms\n2. Select System.Windows.Forms.Button\n3. Click Ok\n4. Move mouse over the new button control that was created'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
