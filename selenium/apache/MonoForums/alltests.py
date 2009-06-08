#!/usr/bin/python
import unittest,sys
sys.path.append('../../..')

from common.monotesting import *

from aaCreateUser import *
from bbCreateForum import *
from ccCreateThread import *

if __name__ == '__main__':
    monotesting_main()
