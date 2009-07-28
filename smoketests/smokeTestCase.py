#!/usr/bin/env python

import sys,os
import unittest
import traceback
import pdb
import glob
import getpass

basepath = os.path.dirname(os.path.realpath(__file__))
while not os.path.isfile(os.path.join(basepath,'common','monoTestCase.py')):
    basepath = os.path.dirname(basepath)
if not basepath in sys.path:
    sys.path.append(basepath)

import common.monotesting as mono
from common.helpers import *
from common.monoTestCase import monoTestCase


####################################################################
#
#    smokeTestCase class
#

class smokeTestCase(monoTestCase):
    testcaseid = 0

    def __init__(self,methodname='runTest'):
        if isAppliance():
            if getpass.getuser() != "root":
                raise Exception("You must run this script as root")

        monoTestCase.__init__(self,methodname)
        self.verificationErrors = []
        unittest.TestCase.__init__(self, methodname)


    def remove(self,filepath):
        if os.path.exists(filepath):
            os.remove(filepath)

    def __printResults(self,tmpfiles,filetype,expected=True):
        expected = "%s" % (['Unexpected','Missing'][expected])
        if len(tmpfiles) > 0:
            print ''
        for f in tmpfiles:
            print "   %s %s: %s" % (expected,filetype,f)
        self.assertEqual(0,len(tmpfiles),"%d %s %ss"% (len(tmpfiles),expected.lower(),filetype))

    #---------------------------------------------------------------
    # keep these around just in case

    def checkList(self,alist,func,filetype,expected):
        errors = []
        for cur in alist:
            if func(cur) ^ expected:
                errors.append(cur)
        self.__printResults(errors,filetype,expected)

    def checkFiles(self,list):
        self.checkList(list,os.path.isfile,'file',expected=True)

    def checkDirs(self,list):
        self.checkList(list,os.path.isdir,'dir',expected=True)

    def checkSymlinks(self, list):
        self.checkList(list,os.path.islink,'symlink',expected=True)

    def checkUnexpectedFiles(self,list):
        self.checkList(list,os.path.isfile,'file',expected=False)

    def checkUnexpectedDirs(self,list):
        self.checkList(list,os.path.isdir,'dir',expected=False)

    def checkUnexpectedSymlinks(self,list):
        self.checkList(list,os.path.islink,'symlink',expected=False)

    #---------------------------------------------------------------

    def checkForList(self, dict, chkFunc):
        #pdb.set_trace()
        for curDirGlob in dict.keys():
            globList = glob.glob(curDirGlob)
            self.assertNotEqual(globList, [], "[%s] either doesn't exist, or is an empty directory." % curDirGlob)
            for curDir in globList:
                # check that the expected files exist
                for curFile in dict[curDirGlob]:
                    for wholeFile in glob.glob(os.path.join(curDir, curFile)):
                        
                        self.assertTrue(chkFunc(wholeFile),"[%s] Not Found." % wholeFile)

                # check that there aren't any unexpected files that exist
                filesInDir = glob.glob(curDir + os.sep + "*")
                for curFile in filesInDir:
                    if chkFunc(curFile):
                        fileNameOnly = os.path.basename(curFile)
                        self.assertTrue(fileNameOnly in dict[curDirGlob], "[%s] unexpectedly exists." % curFile)

    def checkForFiles(self,fileDict):
        self.checkForList(fileDict, os.path.isfile)

    def checkForSymlinks(self,symlinksDict):
        self.checkForList(symlinksDict, os.path.islink)
    #---------------------------------------------------------------
    # These are functions mostly for the vmware test cases
    def getFileSize(self, filePath):
        statinfo = os.stat(filePath)
        return int(statinfo.st_size)

    def getActiveSwapSize(self):
        cmdOut = executeCmd("free -m")
        return int(cmdOut[3].split()[1])

    def areZypperRepoRefreshesOff(self):
        cmdOut = executeCmd("zypper lr")[2:-1]
        for curRefresh in cmdOut:
            self.assertEqual(curRefresh.split()[-1], "No")

    def canZypperReposBeRefreshed(self):
        cmdOut = executeCmd("zypper ref")[-2].strip()
        self.assertEqual(cmdOut, "All repositories have been refreshed.")

    #---------------------------------------------------------------
def generateFileList(basepath,filename):
    f = open(filename,'w')
    files = {}
    symlinks = {}
    for curWalkDirEntries  in os.walk(basepath):
        curWalkDir = curWalkDirEntries[0]
        curWalkFiles = curWalkDirEntries[2]

        filesInCurDir = []
        linksInCurDir = []
        for curFileInDir in curWalkFiles:
            fullPath = os.path.join(curWalkDir, curFileInDir)
            if os.path.isfile(fullPath):
                filesInCurDir.append(curFileInDir)
            elif os.path.islink(fullPath):
                linksInCurDir.append(curFileInDir)
            else:
                raise Exception("%s is not a file or link" % fullPath)

        files[curWalkDir] = filesInCurDir
        symlinks[curWalkDir] = linksInCurDir

    f.write("\nimport os")
    f.write("\nbasepath = '%s'\n" % basepath)
    f.write("\nfiles = {",)
    for curKey in files.keys():
        if len(files[curKey]) > 0:
            newPathList = curKey.replace(basepath,"").split(os.path.sep)[1:]

#            # make it so that the gac checks will pass, even if the gac UUID changes
#            if "gac" in newPathList:
#                newPathList[-1] = "*"

            f.write("\n    os.path.join(basepath")
            for curPath in newPathList:
                f.write(", '%s'" % curPath)
            f.write("):[")
            for curFile in files[curKey]:
                f.write("'%s'," % (curFile))
            f.write("],")
    f.write("\n}\n")

    f.write("\nsymlinks = {")
    for curKey in symlinks.keys():
        if len(symlinks[curKey]) > 0:
            newPathList = curKey.replace(basepath,"").split(os.path.sep)[1:]
            f.write("\n    os.path.join(basepath")
            for curPath in newPathList:
                f.write(", '%s'" % curPath)
            f.write("):[")
            for curFile in symlinks[curKey]:
                f.write("'%s'," % (curFile))
            f.write("],")
    f.write("\n}\n\n")

    f.close()

# vim:ts=4:expandtab:
