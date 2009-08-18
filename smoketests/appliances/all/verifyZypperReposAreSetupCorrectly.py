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
            expectedRepoData = { "MonoVS_SLE-11": ("MonoVS_SLE-11","Yes","Yes","http://go-mono.com/monovs-download/latest/SLE_11?credentials=MonoVS") }
            # We no longer ship with creds
            # expectedCredentials = { "/etc/zypp/credentials.d/MonoVS": (("username","mono-vsbeta"),("password","VfSpW8lIPQ")) }
            expectedCredentials = {}
        else:
            expectedRepoData = { "Mono:Community_11.1+Mono": ("Mono:Community_11.1+Mono","Yes","No","http://download.opensuse.org/repositories/Mono:/Community/openSUSE_11.1+Mono"),
                  "Mono:Community_11.1+Mono:Preview": ("Mono:Community_11.1+Mono:Preview","No","No","http://download.opensuse.org/repositories/Mono:/Community/openSUSE_11.1+Mono_Preview"),
                  "Virtualization:VMware_11.1_Update": ("Virtualization:VMware_11.1_Update","Yes","No","http://download.opensuse.org/repositories/Virtualization:/VMware/openSUSE_11.1_Update/"),
                  "mono-preview-11.1": ("mono-preview-11.1","No","No","http://mono.ximian.com/monobuild/preview/download-preview/openSUSE_11.1/"),
                  "mono-stable-11.1": ("mono-stable-11.1","Yes","No","http://ftp.novell.com/pub/mono/download-stable/openSUSE_11.1"),
                  "openSUSE_11.1_Updates": ("openSUSE_11.1_Updates","Yes","No","http://download.opensuse.org/update/11.1/"),
                  "openSUSE_11.1_oss": ("openSUSE_11.1_oss","Yes","No","http://download.opensuse.org/distribution/11.1/repo/oss/") }
            expectedCredentials = {}

        self.verifyZypperRepoData(expectedRepoData)

        for curCred in expectedCredentials.keys():
            self.verifyZypperCredentials(curCred, expectedCredentials[curCred])

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
