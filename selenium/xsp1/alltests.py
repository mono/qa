#!/usr/bin/python
import sys



sys.path.append('../..')
from common.monotesting import *

# sub directories
# Add child test suites to test suite
#from auth.alltests import *
#from databinding.alltests import *
from web_service.alltests import *
#from handlers.alltests import *
#from customcontrols.alltests import *
#from htmlcontrols.alltests import *
#from webcontrols.alltests import *
#from asp_net_framework import *


if __name__ == '__main__':
    monotesting_main()
