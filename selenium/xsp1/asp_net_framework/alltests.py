#!/usr/bin/python
import unittest

from browserCaps import *
from codeBehind1 import *
from codeRender import *
from includeTest import *
from registerTest import *
from serialTest import *
from serverSideObject import *
from session1 import *
from transferTest import *
from typeDesc import *

sys.path.append('../../../..')
import common.monotesting as mono

if __name__ == '__main__':
    mono.monotesting_main()
