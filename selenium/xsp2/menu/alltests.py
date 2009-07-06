#!/usr/bin/python
import sys,unittest

from menu1Test import *
from menu2Test import *


sys.path.append('../../..')
from common.monotesting import *


if __name__ == '__main__':
    monotesting_main()

# vim:ts=4:expandtab:
