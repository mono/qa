#!/usr/bin/python
import sys

sys.path.append('../..')
from common.monotesting import *

# sub directories
# Add child test suites to test suite

from banshee.alltests import *
from fspot.alltests import *
from monodevelop.alltests import *
from tomboy.alltests import *
from gnomedo.alltests import *
from gbrainy.alltests import *


if __name__ == '__main__':
    monotesting_main()


# vim:ts=4:expandtab:
