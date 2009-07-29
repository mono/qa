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


class verifyWebSiteIconsData(smokeTestCase):
    testcaseid = 869512

    def test(self):
        iconPath = "/home/rupert/Desktop/Mono Web Sites"
        icons = [ ("Banshee.desktop",("URL","http://banshee-project.org/"),("Name","Banshee"),("Type","Link")),
                  ("F-Spot.desktop",("URL","http://f-spot.org/"),("Name","F-Spot"),("Type","Link")),
                  ("gbrainy.desktop",("URL","http://live.gnome.org/gbrainy/"),("Name","gbrainy"),("Type","Link")),
                  ("MonoDevelop.desktop",("URL","http://www.monodevelop.com/"),("Name","MonoDevelop"),("Type","Link")),
                  ("Monologue.desktop",("URL","http://www.go-mono.com/monologue/"),("Name","Monologue - Voices of the Mono Project"),("Type","Link")),
                  ("Mono Project.desktop",("URL","http://www.mono-project.org/"),("Name","Mono Project"),("Type","Link")),
                  ("Monsoon.desktop",("URL","http://www.monsoon-project.org/"),("Name","Monsoon"),("Type","Link")),
                  ("Tomboy.desktop",("URL","http://www.gnome.org/projects/tomboy/"),("Name","Tomboy"),("Type","Link")) ]

        self.verifyOnlyExpectedDesktopFilesExist(iconPath, icons)
        for curIcon in icons:
            self.verifyDesktopFileData(iconPath, curIcon[0], curIcon[1:])

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
