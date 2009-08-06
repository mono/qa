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


class verifyGtkSharpApplicationIconsData(smokeTestCase):
    testcaseid = 869515

    def test(self):
        iconPath = "/home/rupert/Desktop/Gtk# Applications"
        icons = [ ("banshee-1.desktop", ("Exec","banshee-1 --redirect-log --play-enqueued %U"),("Name","Banshee"),("Type","Application")),
                  ("f-spot.desktop",("Exec","f-spot"),("Name","F-Spot"),("Type","Application")),
                  ("gbrainy.desktop",("Exec","gbrainy"),("Name","gbrainy"),("Type","Application")),
                  ("gnome-do.desktop",("Exec","gnome-do"),("Name","GNOME Do"),("Type","Application")),
                  ("monsoon.desktop",("Exec","monsoon"),("Name","Monsoon"),("Type","Application")),
                  ("smuxi-frontend-gnome.desktop",("Exec","smuxi-frontend-gnome"),("Name","Smuxi"),("Type","Application")),
                  ("tasque.desktop",("Exec","tasque"),("Name","Tasque"),("Type","Application")),
                  ("tomboy.desktop",("Exec","tomboy --search"),("Name","Tomboy Notes"),("Type","Application")) ]

        self.verifyOnlyExpectedDesktopFilesExist(iconPath, icons)
        for curIcon in icons:
            self.verifyDesktopFileData(iconPath, curIcon[0], curIcon[1:])

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
