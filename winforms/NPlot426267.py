#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_NPlot426267Test(winformsTestCase):
    testcaseid = 426267
    command = 'NPlot'
    message = 'Run the PlotSurface2D Demo\nMoving mouse over first graph should have a line tracing the mouse position\nZoom in on the first graph (sound wave)\nClick and highlight a section to zoom in.'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
