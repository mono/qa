#!/usr/bin/python
import unittest

from arrayTest import *
from attributeTest import *
from classTest import *
from templateTest import *

sys.path.append('../..')
from monotesting import *

if __name__ == '__main__':
    monotesting_main()
