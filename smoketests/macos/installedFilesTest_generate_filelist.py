#!/usr/bin/env python

import sys
import os
from glob import glob

basepath = os.path.dirname(os.path.realpath(__file__))
while not os.path.isfile(os.path.join(basepath,'common','monoTestCase.py')):
    basepath = os.path.dirname(basepath)
if not basepath in sys.path:
    sys.path.append(basepath)

from smoketests import smokeTestCase

basepath = glob('/Library/Frameworks/Mono.framework/Versions/*')[0]

if __name__ == '__main__':
    filename = 'installedFilesTest_filelist.py'
    smokeTestCase.generateFileList(basepath,filename)
