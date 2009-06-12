#!/usr/bin/env python

import pdb
import subprocess
import unittest


class vmware_unit_tests(unittest.TestCase):
    def __init__(self, methodname="runTest"):
        cmdOut = self.__execute("whoami")
        if cmdOut[0].strip() != "root":
            raise "You must run this script as root"
        unittest.TestCase.__init__(self, methodname)

    def __execute(self, command):
        ret = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        output = ret.communicate()[0]
        lines = output.split('\n')
        return lines

    def setUp(self):
        pass

    def testSwapFileSize(self):
        # Testcase 546301
        cmdOut = self.__execute("ls -lh /swap")
        swapFileSize = cmdOut[0].split()[4]
        self.assertEqual(swapFileSize, "512M")

    def testSwapFileActive(self):
        # Testcase 546302
        cmdOut = self.__execute("free -m")
        swapSize = cmdOut[3].split()[1]
        self.assertEqual(swapSize, "511")

    def testRepoRefreshesAreOff(self):
        # Testcase 546312
        cmdOut = self.__execute("zypper lr")[2:-1]
        for curRefresh in cmdOut:
            self.assertEqual(curRefresh.split()[-1], "No")

    def testRepoRefresh(self):
        # Testcase 546327
        cmdOut = self.__execute("zypper ref")
        self.assertEqual(cmdOut[-2].strip(), "All repositories have been refreshed.")

    def testRepoSettings(self):
        # Testcase 828169
        cmdOut = self.__execute("zypper lr -u")[2:-1]
        numVerifiedRepos = 0
        repos = { "Mono:Community_11.1+Mono": ("Mono:Community_11.1+Mono","Yes","No","http://download.opensuse.org/repositories/Mono:/Community/openSUSE_11.1+Mono"),
                  "Mono:Community_11.1+Mono:Preview": ("Mono:Community_11.1+Mono:Preview","No","No","http://download.opensuse.org/repositories/Mono:/Community/openSUSE_11.1+Mono_Preview"),
                  "Virtualization:VMware_11.1_Update": ("Virtualization:VMware_11.1_Update","Yes","No","http://download.opensuse.org/repositories/Virtualization:/VMware/openSUSE_11.1_Update/"),
                  "mono-preview-11.1": ("mono-preview-11.1","No","No","http://mono.ximian.com/monobuild/preview/download-preview/openSUSE_11.1/"),
                  "mono-stable-11.1": ("mono-stable-11.1","Yes","No","http://ftp.novell.com/pub/mono/download-stable/openSUSE_11.1/"),
                  "openSUSE_11.1_Updates": ("openSUSE_11.1_Updates","Yes","No","http://download.opensuse.org/update/11.1/"),
                  "openSUSE_11.1_oss": ("openSUSE_11.1_oss","Yes","No","http://download.opensuse.org/distribution/11.1/repo/oss/") }

        for curLine in cmdOut:
            curRepo = curLine.split("|")
            alias = curRepo[1].strip()
            name = curRepo[2].strip()
            enabled = curRepo[3].strip()
            refresh = curRepo[4].strip()
            uri = curRepo[5].strip()
            numVerifiedRepos += 1
            self.assertEqual(name, repos[alias][0])
            self.assertEqual(enabled, repos[alias][1])
            self.assertEqual(refresh, repos[alias][2])
            self.assertEqual(uri, repos[alias][3])
        self.assertEqual(numVerifiedRepos, 7)

    def testDiskSize(self):
        # Testcase 546325
        cmdOut = self.__execute("df -h")
        diskSize = cmdOut[1].split()[1]
        self.assertEqual(diskSize, "30G")

    def testHelloWorldAspxSite(self):
        # Testcase 816722
        cmdOut = self.__execute("export TSTSTR=tc816722-$(uuidgen) ;" +
                                "export WEBDIR=/srv/www/htdocs/$TSTSTR ;" +
                                "export TMPDIR=/tmp/$TSTSTR ;" +
                                "mkdir -p $WEBDIR ;" +
                                "echo '<html><body><p><%= \"Hello World!\" %></p></body></html>' > $WEBDIR/index.aspx ;" +
                                "mkdir -p $TMPDIR ;" +
                                "cd $TMPDIR ;" +
                                "wget http://localhost/$TSTSTR > /dev/null 2>&1 ;" +
                                "cat index.html ;" +
                                "rm -rf $WEBDIR ;" +
                                "rm -rf $TMPDIR")
        self.assertEqual(cmdOut[0].strip(), "<html><body><p>Hello World!</p></body></html>")

    def __checkDesktopFile(self, file, icons, iconPath):
        if icons[file][2] == "Type=Application":
            action = self.__execute("cd " + iconPath + "; grep '^Exec=' '" + file + "'")[0]
        elif icons[file][2] == "Type=Link":
            action = self.__execute("cd " + iconPath + "; grep '^URL=' '" + file + "'")[0]

        name = self.__execute("cd " + iconPath + "; grep '^Name=' '" + file + "'")[0]
        type = self.__execute("cd " + iconPath + "; grep '^Type=' '" + file + "'")[0]
        self.assertEqual(action, icons[file][0])
        self.assertEqual(name, icons[file][1])
        self.assertEqual(type, icons[file][2])

    def testGtkSharpApplicationsIconsData(self):
        # Testcase 869515
        iconPath = "/home/rupert/Desktop/Gtk#\ Applications"
        cmdOut = self.__execute("cd " + iconPath + ";for FILE in *; do echo $FILE; done")
        icons = { "banshee-1.desktop":("Exec=banshee-1 --redirect-log --play-enqueued %U","Name=Banshee","Type=Application"),
                  "f-spot.desktop":("Exec=f-spot","Name=F-Spot","Type=Application"),
                  "gbrainy.desktop":("Exec=gbrainy","Name=gbrainy","Type=Application"),
                  "gnome-do.desktop":("Exec=gnome-do","Name=GNOME Do","Type=Application"),
                  "monsoon.desktop":("Exec=monsoon","Name=Monsoon","Type=Application"),
                  "smuxi-frontend-gnome.desktop":("Exec=smuxi-frontend-gnome","Name=Smuxi","Type=Application"),
                  "tasque.desktop":("Exec=tasque","Name=Tasque","Type=Application"),
                  "tomboy.desktop":("Exec=tomboy --search","Name=Tomboy Notes","Type=Application") }

        for curFile in cmdOut[0:-1]:
            self.__checkDesktopFile(curFile, icons, iconPath)

    def testWebSiteIconsData(self):
        # Testcase 869512
        iconPath = "/home/rupert/Desktop/Mono\ Web\ Sites"
        cmdOut = self.__execute("cd " + iconPath + ";for FILE in *; do echo $FILE; done")
        icons = { "Banshee.desktop":("URL=http://banshee-project.org/","Name=Banshee","Type=Link"),
                  "F-Spot.desktop":("URL=http://f-spot.org/","Name=F-Spot","Type=Link"),
                  "gbrainy.desktop":("URL=http://live.gnome.org/gbrainy/","Name=gbrainy","Type=Link"),
                  "MonoDevelop.desktop":("URL=http://www.monodevelop.com/","Name=MonoDevelop","Type=Link"),
                  "Monologue.desktop":("URL=http://www.go-mono.com/monologue/","Name=Monologue - Voices of the Mono Project","Type=Link"),
                  "Mono Project.desktop":("URL=http://www.mono-project.org/","Name=Mono Project","Type=Link"),
                  "Monsoon.desktop":("URL=http://www.monsoon-project.org/","Name=Monsoon","Type=Link"),
                  "Tomboy.desktop":("URL=http://www.gnome.org/projects/tomboy/","Name=Tomboy","Type=Link") }

        for curFile in cmdOut[0:-1]:
            self.__checkDesktopFile(curFile, icons, iconPath)

    def testWebAppIconsData(self):
        # Testcase 869516
        iconPath = "/home/rupert/Desktop/Mono\ Web\ Applications"
        cmdOut = self.__execute("cd " + iconPath + ";for FILE in *; do echo $FILE; done")
        icons = { "about.desktop":("URL=file:///srv/www/htdocs/index.html","Name=About ASP.NET Applications","Type=Link"),
                  "AspNetForums.desktop":("URL=http://localhost/AspNetForums/","Name=ASP.NET Forums","Type=Link"),
                  "BlogStarterKit.desktop":("URL=http://localhost/BlogStarterKit/Admin/","Name=Blog Starter Kit","Type=Link"),
                  "ClassifiedsStarterKit.desktop":("URL=http://localhost/ClassifiedsStarterKit/default.aspx","Name=Classifieds Starter Kit","Type=Link"),
                  "ClubWebSite.desktop":("URL=http://localhost/ClubWebSite/","Name=Club Web Site Starter Kit","Type=Link"),
                  "mojoPortal.desktop":("URL=http://localhost/mojoportal/","Name=mojoPortal Web Site Framework","Type=Link"),

                  "sources.desktop":("URL=file:///usr/share/mono/asp.net","Name=Sources","Type=Link") }

        for curFile in cmdOut[0:-1]:
            self.__checkDesktopFile(curFile, icons, iconPath)

    def testWinformsApplicationsIconsData(self):
        # Testcase 869519
        iconPath = "/home/rupert/Desktop/Mono\ Winforms\ Applications"
        cmdOut = self.__execute("cd " + iconPath + ";for FILE in *; do echo $FILE; done")
        icons = { "AderPlotter.desktop":("Exec=AderPlotter","Name=AderPlotter","Type=Application"),
                  "AnotherTetrisClone.desktop":("Exec=AnotherTetrisClone","Name=AnotherTetrisClone","Type=Application"),
                  "ChessBoard.desktop":("Exec=ChessBoard","Name=ChessBoard","Type=Application"),
                  "ControlInspector.desktop":("Exec=ControlInspector","Name=ControlInspector","Type=Application"),
                  "CSharpTetris.desktop":("Exec=CSharpTetris","Name=CSharpTetris","Type=Application"),
                  "GATetris.desktop":("Exec=GATetris","Name=GATetris","Type=Application"),
                  "GraphLibraryDemo.desktop":("Exec=GraphLibraryDemo","Name=GraphLibraryDemo","Type=Application"),
                  "ICanSpy.desktop":("Exec=ICanSpy","Name=ICanSpy","Type=Application"),
                  "IEClone.desktop":("Exec=IEClone","Name=IEClone","Type=Application"),
                  "MonoCalendar.desktop":("Exec=MonoCalendar","Name=MonoCalendar","Type=Application"),
                  "myUML.desktop":("Exec=myUML","Name=myUML","Type=Application"),
                  "Notepad.desktop":("Exec=Notepad","Name=Notepad","Type=Application"),
                  "NPlot.desktop":("Exec=NPlot","Name=NPlot","Type=Application"),
                  "PieChart.desktop":("Exec=PieChart","Name=PieChart","Type=Application"),
                  "PolygonTriangulation.desktop":("Exec=PolygonTriangulation","Name=PolygonTriangulation","Type=Application"),
                  "ReportBuilder.desktop":("Exec=ReportBuilder","Name=ReportBuilder","Type=Application"),
                  "Rubik.desktop":("Exec=Rubik","Name=Rubik","Type=Application"),
                  "SharpChess.desktop":("Exec=SharpChess","Name=SharpChess","Type=Application"),
                  "sources.desktop":("URL=file:///home/rupert/src","Name=Sources","Type=Link"),
                  "SplineInterpolation.desktop":("Exec=SplineInterpolation","Name=SplineInterpolation","Type=Application"),
                  "SVGPad.desktop":("Exec=SVGPad","Name=SVGPad","Type=Application"),
                  "UsingWebBrowser.desktop":("Exec=UsingWebBrowser","Name=UsingWebBrowser","Type=Application") }

        for curFile in cmdOut[0:-1]:
            self.__checkDesktopFile(curFile, icons, iconPath)

    def testWinformsApplicationsIconsData(self):
        # Testcase 869520
        iconPath = "/home/rupert/Desktop/"
        cmdOut = self.__execute("cd " + iconPath + ";for FILE in *.desktop; do echo $FILE; done")
        icons = { "moma.desktop":("Exec=moma","Name=MoMA","Type=Application"),
                  "monodevelop.desktop":("Exec=monodevelop","Name=Mono Development Environment","Type=Application"),
                  "monodoc.desktop":("Exec=/usr/bin/monodoc","Name=Mono Documentation","Type=Application"),
                  "start-here.desktop":("URL=file:///srv/www/htdocs/index.html","Name=Start Here","Type=Link") }

        for curFile in cmdOut[0:-1]:
            self.__checkDesktopFile(curFile, icons, iconPath)

if __name__ == "__main__":
    unittest.main()

# vim:ts=4:expandtab:
