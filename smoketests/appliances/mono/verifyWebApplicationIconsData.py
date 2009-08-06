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


class verifyWebApplicationIconsData(smokeTestCase):
    testcaseid = 869516

    def test(self):
        iconPath = "/home/rupert/Desktop/Mono Web Applications"
        icons = [ ("about.desktop",("URL","file:///srv/www/htdocs/index.html"),("Name","About ASP.NET Applications"),("Type","Link")),
                  ("AspNetForums.desktop",("URL","http://localhost/AspNetForums/"),("Name","ASP.NET Forums"),("Type","Link")),
                  ("BlogStarterKit.desktop",("URL","http://localhost/BlogStarterKit/Admin/"),("Name","Blog Starter Kit"),("Type","Link")),
                  ("ClassifiedsStarterKit.desktop",("URL","http://localhost/ClassifiedsStarterKit/default.aspx"),("Name","Classifieds Starter Kit"),("Type","Link")),
                  ("ClubWebSite.desktop",("URL","http://localhost/ClubWebSite/"),("Name","Club Web Site Starter Kit"),("Type","Link")),
                  ("mojoPortal.desktop",("URL","http://localhost/mojoportal/"),("Name","mojoPortal Web Site Framework"),("Type","Link")),
                  ("sources.desktop",("URL","file:///usr/share/mono/asp.net"),("Name","Sources"),("Type","Link")) ]

        self.verifyOnlyExpectedDesktopFilesExist(iconPath, icons)
        for curIcon in icons:
            self.verifyDesktopFileData(iconPath, curIcon[0], curIcon[1:])

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
