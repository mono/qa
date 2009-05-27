#!/usr/bin/python
import unittest,sys

from tabcontrolTest import *
from tabcontrol2Test import *

sys.path.append('../../../..')
import common.monotesting as mono

if __name__ == '__main__':
    mono.monotesting_main()
