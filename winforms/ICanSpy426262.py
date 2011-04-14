#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('..')
import common.monotesting as mono
from winformsTestCase import winformsTestCase


class WinForms_ICanSpy426262Test(winformsTestCase):
    testcaseid = 426262
    command = 'ICanSpy'
    message = 'Inspect GATetris main form\n1. Click File / Select Form\n2. Click browse\n3. Navigate to /usr/lib/GATetris\n4. Select GATetris.exe\n5. Click Open\n6. Click Ok\n7. Click File / Select Events\n8. Click the checkbox next to GATetrisControl.TetrisGrid\n9. Click Ok\n10. Click File / Start Logging\n11. Move your mouse over GATetris GameForm\n12. Notice the events are logged\n13. Click File / Stop Logging\n14. Exit ICanSpy'


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
