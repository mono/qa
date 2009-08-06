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


class verifyExpectedRpmsAreInstalled(smokeTestCase):
    testcaseid = 871305

    def test(self):
        expectedRpms = [ "mono-core",
                         "mono-devel",
                         "mono-debugger",
                         "mono-check",
                         "mono-addins",
                         "mono-nunit",
                         "mono-locale-extras",
                         "mono-zeroconf",
                         "mono-zeroconf-doc",
                         "mono-tools",
                         "mono-complete",
                         "mono-extras",
                         "monodoc-core",
                         "mono-wcf",
                         "mono-basic",
                         "mono-winfxcore",
                         "mono-jscript",
                         "mono-zeroconf-provider-avahi",
            # --------------------------------------------
                         "mono-winforms",
                         "libgdiplus0",
                         "libgluezilla0",
            # --------------------------------------------
                         "mono-web",
                         "apache2-mod_mono",
                         "Mono_ASP.NET_MonoForums",
                         "Mono_ASP.NET_ClubWebSite",
                         "Mono_ASP.NET_ClassifiedsStarterKit",
                         "Mono_ASP.NET_BlogStarterKit",
            # --------------------------------------------
                         "mono-data",
                         "mono-data-oracle",
                         "mono-data-sqlite",
                         "mono-data-postgresql",
                         "mono-data-sybase",
                         "mono-data-firebird",
                         "bytefx-data-mysql",
                         "ibm-data-db2",
            # --------------------------------------------
                         "monodevelop",
                         "monodevelop-boo",
                         "monodevelop-database",
                         "monodevelop-debugger-gdb",
                         "monodevelop-debugger-mdb",
                         "monodevelop-java",
                         "monodevelop-vala",
            # --------------------------------------------
                         "mono-uia",
                         "uiaatkbridge",
                         "uiautomationwinforms",
            # --------------------------------------------
                         "gmime-sharp",
                         "gtkhtml314-sharp",
                         "webkit-sharp",
                         "gnome-sharp2-complete",
                         "gecko-sharp2",
                         "gnome-print-sharp",
                         "gnome-desktop-sharp2",
                         "taglib-sharp",
                         "gtk-sharp2",
                         "gnome-vfs-sharp2",
                         "glade-sharp2",
                         "gnome-sharp2",
                         "rsvg2-sharp",
                         "vte016-sharp",
                         "gtk-sharp2-complete",
                         "gtk-sharp2-gapi",
                         "gnome-keyring-sharp",
                         "gtksourceview-sharp2",
                         "gnome-panel-sharp",
                         "nautilusburn-sharp",
                         "glib-sharp2",
                         "gtk-sharp2-doc",
                         "evolution-sharp",
                         "art-sharp2",
                         "gconf-sharp2",
                         "notify-sharp",
                         "wnck-sharp",
                         "gtksourceview2-sharp",
            # --------------------------------------------
                         "IPCE",
                         "boo",
                         "boo-devel",
                         "ikvm",
                         "nant",
                         "ndesk-dbus",
                         "ndesk-dbus-glib",
                         "ndesk-dbus-glib-devel",
                         "webkit-sharp",
                         "xsp" ]

        self.verifyTheseRpmsAreInstalled(expectedRpms)

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
