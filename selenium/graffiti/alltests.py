#!/usr/bin/python
import sys

sys.path.append('../..')
from common.monotesting import *

# sub directories
# Add child test suites to test suite

from aaCreateUser import *
from bbCreateBlogPost import *
from ccCreateSampleContent import *
from ddApprovePosts import *
from ee_deletePosts import *
from ff_purgePost1 import *
from gg_purgePost2 import *

if __name__ == '__main__':
    monotesting_main()

# vim:ts=4:expandtab:
