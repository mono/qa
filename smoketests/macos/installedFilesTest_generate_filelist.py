#!/usr/bin/python

import os
from glob import glob

import sys
sys.path.append("..")
import smokeTestCase

basepath = glob('/Library/Frameworks/Mono.framework/Versions/*')[0]

if __name__ == '__main__':
    filename = 'installedFilesTest_filelist.py'
    smokeTestCase.generateFileList(basepath,filename)