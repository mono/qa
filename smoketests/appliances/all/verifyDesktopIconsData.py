#!/usr/bin/env python

import sys, unittest, os

basepath = os.path.dirname(os.path.realpath(__file__))
while not os.path.isfile(os.path.join(basepath,'common','monoTestCase.py')):
    basepath = os.path.dirname(basepath)
if not basepath in sys.path:
    sys.path.append(basepath)

import common.monotesting as mono
from smoketests.smokeTestCase import smokeTestCase
from common.helpers import *


class verifyDesktopIconsData(smokeTestCase):
    testcaseid = 869520

    def test(self):
        userDesktopPath = "/home/rupert/Desktop/"
        distDesktopPath = "/usr/share/dist/desktop-files"

        if isMonoVSAppliance():
            userDesktopIcons = []
            distDesktopIcons = [ ("monovs-server.desktop",("Exec","monovs-gui-server"),("Name","MonoVS Server"),("Icon","monovs-server"),("Type","Application")),
                  ("monovs-server-version.desktop",("Exec","monovs-server-version"),("Name","MonoVS Server Version"),("Icon","dialog-question"),("Type","Application")),
                  ("update-monovs.desktop",("Exec","update-monovs"),("Name","Update MonoVS Server"),("Icon","up"),("Type","Application")) ]
        else:
            userDesktopIcons = [ ("moma.desktop",("Exec","moma"),("Name","MoMA"),("Icon","moma48"),("Type","Application")),
                  ("monodevelop.desktop",("Exec","monodevelop"),("Name","Mono Development Environment"),("Icon","monodevelop"),("Type","Application")),
                  ("monodoc.desktop",("Exec","/usr/bin/monodoc"),("Name","Mono Documentation"),("Icon","monodoc"),("Type","Application")),
                  ("start-here.desktop",("URL","file:///srv/www/htdocs/index.html"),("Name","Start Here"),("Icon","mono"),("Type","Link")) ]
            distDesktopIcons = [ ("GnomeOnlineHelp.desktop",("URL","http://help.opensuse.org/"),("Name","Online Help"),("Icon","/usr/share/dist/icons/suse-help.svg"),("Type","Link")),
                  ("SuSE.desktop",("URL","http://www.opensuse.org/"),("Name","openSUSE"),("Icon","suse"),("Type","Link")) ]


        self.verifyOnlyExpectedDesktopFilesExist(userDesktopPath, userDesktopIcons)
        for curIcon in userDesktopIcons:
            self.verifyDesktopFileData(userDesktopPath, curIcon[0], curIcon[1:])

        self.verifyOnlyExpectedDesktopFilesExist(distDesktopPath, distDesktopIcons)
        for curIcon in distDesktopIcons:
            self.verifyDesktopFileData(distDesktopPath, curIcon[0], curIcon[1:])

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
