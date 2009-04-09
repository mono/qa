#!/usr/bin/python
import unittest,sys
sys.path.append('../../..')

from common.monotesting import *

from asyncTest import *
from chunkedTest import *
from emptyTest import *
from monodocTest import *
from webhandlerTest import *

if __name__ == '__main__':
    monotesting_main()
