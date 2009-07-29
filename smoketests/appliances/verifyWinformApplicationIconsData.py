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


class verifyWinformApplicationIconsData(smokeTestCase):
    testcaseid = 869519

    def test(self):
        iconPath = "/home/rupert/Desktop/Mono Winforms Applications"
        icons = [ ("AderPlotter.desktop",("Exec","AderPlotter"),("Name","AderPlotter"),("Type","Application")),
                  ("AnotherTetrisClone.desktop",("Exec","AnotherTetrisClone"),("Name","AnotherTetrisClone"),("Type","Application")),
                  ("ChessBoard.desktop",("Exec","ChessBoard"),("Name","ChessBoard"),("Type","Application")),
                  ("ControlInspector.desktop",("Exec","ControlInspector"),("Name","ControlInspector"),("Type","Application")),
                  ("CSharpTetris.desktop",("Exec","CSharpTetris"),("Name","CSharpTetris"),("Type","Application")),
                  ("GATetris.desktop",("Exec","GATetris"),("Name","GATetris"),("Type","Application")),
                  ("GraphLibraryDemo.desktop",("Exec","GraphLibraryDemo"),("Name","GraphLibraryDemo"),("Type","Application")),
                  ("ICanSpy.desktop",("Exec","ICanSpy"),("Name","ICanSpy"),("Type","Application")),
                  ("IEClone.desktop",("Exec","IEClone"),("Name","IEClone"),("Type","Application")),
                  ("MonoCalendar.desktop",("Exec","MonoCalendar"),("Name","MonoCalendar"),("Type","Application")),
                  ("myUML.desktop",("Exec","myUML"),("Name","myUML"),("Type","Application")),
                  ("Notepad.desktop",("Exec","Notepad"),("Name","Notepad"),("Type","Application")),
                  ("NPlot.desktop",("Exec","NPlot"),("Name","NPlot"),("Type","Application")),
                  ("PieChart.desktop",("Exec","PieChart"),("Name","PieChart"),("Type","Application")),
                  ("PolygonTriangulation.desktop",("Exec","PolygonTriangulation"),("Name","PolygonTriangulation"),("Type","Application")),
                  ("ReportBuilder.desktop",("Exec","ReportBuilder"),("Name","ReportBuilder"),("Type","Application")),
                  ("Rubik.desktop",("Exec","Rubik"),("Name","Rubik"),("Type","Application")),
                  ("SharpChess.desktop",("Exec","SharpChess"),("Name","SharpChess"),("Type","Application")),
                  ("sources.desktop",("URL","file:///home/rupert/src"),("Name","Sources"),("Type","Link")),
                  ("SplineInterpolation.desktop",("Exec","SplineInterpolation"),("Name","SplineInterpolation"),("Type","Application")),
                  ("SVGPad.desktop",("Exec","SVGPad"),("Name","SVGPad"),("Type","Application")),
                  ("UsingWebBrowser.desktop",("Exec","UsingWebBrowser"),("Name","UsingWebBrowser"),("Type","Application")) ]

        self.verifyOnlyExpectedDesktopFilesExist(iconPath, icons)
        for curIcon in icons:
            self.verifyDesktopFileData(iconPath, curIcon[0], curIcon[1:])

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
