#!/usr/bin/env python

import sys, unittest, os

basepath = os.path.dirname(os.path.realpath(__file__))
while not os.path.isfile(os.path.join(basepath,'common','monoTestCase.py')):
    basepath = os.path.dirname(basepath)
if not basepath in sys.path:
    sys.path.append(basepath)

import common.monotesting as mono
from common.helpers import *
from smoketests.smokeTestCase import smokeTestCase


class verifyZypperRepoFilesArentOwnedByRpm(smokeTestCase):
    testcaseid = 828169

    def test(self):

        if isMonoVSAppliance():
            filesToCheck= ["/etc/zypp/repos.d/MonoVS.repo",
                           "/etc/zypp/repos.d/openSUSE_11.1_oss.repo",
                           "/etc/zypp/repos.d/openSUSE_11.1_Updates.repo",
                           "/etc/zypp/repos.d/Virtualization_VMware_11.1_Update.repo"]
        else:
            filesToCheck= ["/etc/zypp/repos.d/Mono_Community_11.1+Mono_Preview.repo",
                           "/etc/zypp/repos.d/Mono:Community_11.2+Mono.repo",
                           "/etc/zypp/repos.d/openSUSE_11.2_Updates.repo",
                           "/etc/zypp/repos.d/openSUSE-11.2-Oss.repo",
                           "/etc/zypp/repos.d/mono-stable-11.2.repo",
                           "/etc/zypp/repos.d/mono-preview-11.2.repo" ]

        for curFile in filesToCheck:
            self.verifyRpmDoesntOwnFile(curFile)

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
