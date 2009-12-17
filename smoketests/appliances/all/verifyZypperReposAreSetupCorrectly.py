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


class verifyZypperReposAreSetupCorrectly(smokeTestCase):
    testcaseid = 828169

    def test(self):

        if isMonoVSAppliance():
            expectedRepoData = { "MonoVS": ("MonoVS","Yes","No","http://ftp.novell.com/pub/mono/monovs/latest/openSUSE_11.1"),
                                 "Virtualization:VMware_11.1_Update": ("Virtualization:VMware_11.1_Update","Yes","No","http://download.opensuse.org/repositories/Virtualization:/VMware/openSUSE_11.1_Update"),
                                 "openSUSE_11.1_Updates": ("openSUSE_11.1_Updates","Yes","No","http://download.opensuse.org/update/11.1"),
                                 "openSUSE_11.1_oss": ("openSUSE_11.1_oss","Yes","No","http://download.opensuse.org/distribution/11.1/repo/oss") }
            expectedCredentials = {}
        else:
            expectedRepoData = { "Mono:Community_11.2+Mono": ("Mono:Community_11.2+Mono","Yes","No","http://download.opensuse.org/repositories/Mono:/Community/openSUSE_11.2+Mono"),
                  "Mono:Community_11.1+Mono:Preview": ("Mono:Community_11.1+Mono:Preview","No","No","http://download.opensuse.org/repositories/Mono:/Community/openSUSE_11.1+Mono_Preview"),
                  "mono-preview-11.2": ("mono-preview-11.2","No","No","http://mono.ximian.com/monobuild/preview/download-preview/openSUSE_11.2"),
                  "mono-stable-11.2": ("mono-stable-11.2","Yes","No","http://ftp.novell.com/pub/mono/download-stable/openSUSE_11.2"),
                  "openSUSE_11.2_Updates": ("openSUSE_11.2_Updates","Yes","No","http://download.opensuse.org/update/11.2"),
                  "openSUSE-11.2-Oss": ("openSUSE-11.2-Oss","Yes","No","http://download.opensuse.org/distribution/11.2/repo/oss") }
            expectedCredentials = {}

        self.verifyZypperRepoData(expectedRepoData)

        for curCred in expectedCredentials.keys():
            self.verifyZypperCredentials(curCred, expectedCredentials[curCred])

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
