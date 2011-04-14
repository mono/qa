#!/usr/bin/python
import sys

sys.path.append('..')
from common.monotesting import *

# sub directories
# Add child test suites to test suite

from AderPlotter426249 import *
from AderPlotter426251 import *
from AnotherTetrisClone426253 import *
from ChessBoard426255 import *
from ChessBoard426256 import *
from ChessBoard426257 import *
from ControlInspector426259 import *
from GATetris433810 import *
from GATetris426260 import *
from GraphLibraryDemo426261 import *
from ICanSpy426262 import *
from IEClone709763 import *
from MoMA496504 import *
from MoMA496505 import *


if __name__ == '__main__':
    monotesting_main()


# vim:ts=4:expandtab:
