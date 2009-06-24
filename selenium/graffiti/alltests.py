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
from eeDeletePosts import *
from ffPurgePost1 import *
from ggPurgePost2 import *
from hhDeleteUser import *

if __name__ == '__main__':
    monotesting_main()

# vim:ts=4:expandtab:
