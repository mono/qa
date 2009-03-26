#!/usr/bin/python
import unittest

from asyncTest import *
from chunkedTest import *
from emptyTest import *
#from monodocTest import *
from webhandlerTest import *


sys.path.append('../..')
from monotesting import *

if __name__ == '__main__':
    monotesting_main()
