#!/usr/bin/python
import sys

sys.path.append('../..')
from common.monotesting import *

# sub directories
# Add child test suites to test suite

sys.path.append('..')
from xsp1.alltests import *

#from masterpages.alltests import *
#from menu.alltests import *
#from treeview.alltests import *


if __name__ == '__main__':
    monotesting_main(xsp1_tmp_port=8082)


# vim:ts=4:expandtab:
