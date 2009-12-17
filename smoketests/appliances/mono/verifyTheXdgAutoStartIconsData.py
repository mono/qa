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


class verifyTheXdgAutoStartIconsData(smokeTestCase):
    testcaseid = 871071

    def test(self):
        iconPath = "/etc/xdg/autostart"
        icons = [ ("gnome-at-session.desktop",("Exec","gnome-at-visual -s"),("Name","Visual Assistance"),("Type","Application")),
                  ("gnome-settings-daemon.desktop",("Exec","/usr/lib/gnome-settings-daemon/gnome-settings-daemon"),("Name","GNOME Settings Daemon"),("Type","Application")),
                  ("gnome-settings-daemon-helper.desktop",("Exec","/usr/lib/gnome-session/helpers/gnome-settings-daemon-helper"), ("Name","GNOME Settings Daemon Helper"), ("Type","Application")),
                  ("gnome-keyring-daemon.desktop",("Exec","gnome-keyring-daemon --start"), ("Name","GNOME Keyring Daemon"), ("Type","Application")),
                  ("gnome-volume-control-applet.desktop",("Exec","gnome-volume-control-applet"), ("Name","Volume Control"), ("Type","Application")),
                  ("gnome-screensaver.desktop",("Exec","gnome-screensaver"), ("Name","Screensaver"), ("Type","Application")),
                  ("at-spi-registryd.desktop",("Exec","/usr/lib/at-spi/at-spi-registryd"), ("Name","AT SPI Registry Wrapper"), ("Type","Application")),
                  ("nm-applet.desktop",("Exec","nm-applet --sm-disable"),("Name","Network Manager"),("Type","Application")),
                  ("pulseaudio.desktop",("Exec","start-pulseaudio-x11"),("Name","PulseAudio Sound System"),("Type","Application")),
                  ("vmware-user-autostart.desktop",("Exec","vmware-user-autostart-wrapper"),("Name","VMware User Agent"),("Type","Application")) ]

        self.verifyOnlyExpectedDesktopFilesExist(iconPath, icons)
        for curIcon in icons:
            self.verifyDesktopFileData(iconPath, curIcon[0], curIcon[1:])

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
