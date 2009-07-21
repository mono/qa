import os
from glob import glob

import sys
sys.path.append("..")
import smokeTestCase

basepath = glob("C:\Program Files\Mono-*")[0]

if __name__ == '__main__':
    smokeTestCase.generateFileListInWindows(basepath)
