#!/usr/bin/python
import sys
import os

basepath = os.path.dirname(os.path.realpath(__file__))
while not os.path.isfile(os.path.join(basepath,'common','monoTestCase.py')):
    basepath = os.path.dirname(basepath)
if not basepath in sys.path:
    sys.path.append(basepath)

from common.monotesting import *

# sub directories
# Add child test suites to test suite
from verifyApacheIsRunning import *
from verifyApacheWebDirPerms import *
from verifyDesktopIconsData import *
from verifyExpectedRpmsAreInstalled import *
from verifyGtkSharpApplicationIconsData import *
from verifyKernelCommandLineOptions import *
from verifyRootDiskInodeCount import *
from verifyRootDiskSize import *
from verifySambaConfigFile import *
from verifySambaIsRunning import *
from verifySampleAspxPageWorks import *
from verifySwapFileIsActive import *
from verifySwapFileSize import *
from verifyTheXdgAutoStartIconsData import *
from verifyVMwareToolsUserAgent import *
from verifyVMwareToolsX11Config import *
from verifyWebApplicationIconsData import *
from verifyWebSiteIconsData import *
from verifyWinformApplicationIconsData import *
from verifyZypperRepoRefreshesAreOff import *
from verifyZypperReposAreSetupCorrectly import *
from verifyZypperReposCanRefresh import *


if __name__ == '__main__':
    monotesting_main()


# vim:ts=4:expandtab:
