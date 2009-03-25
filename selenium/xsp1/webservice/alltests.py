#!/usr/bin/python
import sys,unittest

from addTest import *
from echoTest import *

sys.path.append('../..')
from monotesting import *


if __name__ == '__main__':
    monotesting_main()
