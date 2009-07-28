#!/usr/bin/python
import sys

sys.path.append('../..')
from common.monotesting import *

# sub directories
# Add child test suites to test suite
from areRepoRefreshesOff import *
from canReposRefresh import *
from isSwapFileActive import *
from swapFileSize import *


if __name__ == '__main__':
    monotesting_main()


# vim:ts=4:expandtab:
