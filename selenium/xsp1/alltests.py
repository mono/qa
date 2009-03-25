#!/usr/bin/python
import unittest
import sys

sys.path.append('..')

# sub directories
# Add child test suites to test suite
from webservice.alltests import *
from auth.alltests import *
from databinding.alltests import *
from handlers.alltest import *
from customcontrols.alltest import *


if __name__ == '__main__':
    unittest.main()
