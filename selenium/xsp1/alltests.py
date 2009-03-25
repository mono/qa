#!/usr/bin/python
import unittest
import sys

sys.path.append('..')
from monotesting import *

# sub directories
# Add child test suites to test suite
from webservice.alltests import *
#from auth.alltests import *
from databinding.alltests import *
from handlers.alltests import *
from customcontrols.alltests import *
#from htmlcontrols.alltests import *
#from webcontrols.alltests import *
from asp_net_framework import *


if __name__ == '__main__':
    monotesting_main()
