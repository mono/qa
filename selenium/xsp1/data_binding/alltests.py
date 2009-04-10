#!/usr/bin/python
import unittest,sys
sys.path.append('../../..')

from common.monotesting import *

from arrayTest import *
from attributeTest import *
from classTest import *
from templateTest import *

if __name__ == '__main__':
    monotesting_main()
