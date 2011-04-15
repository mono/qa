#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_UsingWebBrowser556344Test(winformsTestCase):
    testcaseid = 556344
    command = 'UsingWebBrowser'
    message = 'Browse HTML document file\n1. Click on HTML Doc Viewer tab\n2. Default document is /usr/lib/UsingWebBrowser/README.htm\n3. Maker sure there are no rendering errors\n4. Open a seperate HTML document and make sure that it renders.  Possibly a saved web page from slashdot or lwn.net\n5. Make sure that the new document renders correclty\nThis test case does not work for MacOSX'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
