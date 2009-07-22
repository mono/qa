#!/usr/bin/python
import os

import sys
sys.path.append("..")
import smokeTestCase

basepath = '/usr/lib/mono'
filename = 'filelist.py'

if __name__ == '__main__':
    smokeTestCase.generateFileList(basepath,filename)


