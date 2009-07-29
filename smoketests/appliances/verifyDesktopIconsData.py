#!/usr/bin/env python

import sys, unittest, os

basepath = os.path.dirname(os.path.realpath(__file__))
while not os.path.isfile(os.path.join(basepath,'common','monoTestCase.py')):
    basepath = os.path.dirname(basepath)
if not basepath in sys.path:
    sys.path.append(basepath)

import common.monotesting as mono
from smoketests.smokeTestCase import smokeTestCase
from common.helpers import executeCmd


class verifyDesktopIconsData(smokeTestCase):
    testcaseid = 869520

    def test(self):
        iconPath = "/home/rupert/Desktop/"
        icons = [ ("moma.desktop",("Exec","moma"),("Name","MoMA"),("Type","Application")),
                  ("monodevelop.desktop",("Exec","monodevelop"),("Name","Mono Development Environment"),("Type","Application")),
                  ("monodoc.desktop",("Exec","/usr/bin/monodoc"),("Name","Mono Documentation"),("Type","Application")),
                  ("start-here.desktop",("URL","file:///srv/www/htdocs/index.html"),("Name","Start Here"),("Type","Link")) ]

        self.verifyOnlyExpectedDesktopFilesExist(iconPath, icons)
        for curIcon in icons:
            self.verifyDesktopFileData(iconPath, curIcon[0], curIcon[1:])

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
