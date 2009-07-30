#!/usr/bin/env python

import sys, unittest, os, ConfigParser

basepath = os.path.dirname(os.path.realpath(__file__))
while not os.path.isfile(os.path.join(basepath,'common','monoTestCase.py')):
    basepath = os.path.dirname(basepath)
if not basepath in sys.path:
    sys.path.append(basepath)

import common.monotesting as mono
from smoketests.smokeTestCase import smokeTestCase
from common.helpers import executeCmd


class verifySambaConfigFile(smokeTestCase):
    testcaseid = 871296

    def test(self):
        cmdOut = executeCmd("cat /etc/samba/smb.conf |sed -e 's/\t//g' > /tmp/vmware_auto-smb.conf")
        self.assertEqual(len(cmdOut),1)
        config = ConfigParser.ConfigParser()
        config.read("/tmp/vmware_auto-smb.conf")
        self.assertEqual(config.get("global","workgroup"), "MONO")
        self.assertEqual(config.get("global","security"), "user")
        self.assertEqual(config.get("global","passdb backend"), "smbpasswd")
        self.assertEqual(config.get("global","username map"), "/etc/samba/smbusers")
        self.assertEqual(config.get("homes","inherit acls"), "Yes")
        self.assertEqual(config.get("homes","browseable"), "No")
        self.assertEqual(config.get("homes","read only"), "No")
        self.assertEqual(config.get("htdocs","inherit acls"), "Yes")
        self.assertEqual(config.get("htdocs","browseable"), "Yes")
        self.assertEqual(config.get("htdocs","path"), "/srv/www/htdocs/")
        self.assertEqual(config.get("htdocs","read only"), "No")

        cmdOut = executeCmd("cat /etc/samba/smbpasswd|grep rupert")[0].split(':')
        self.assertEqual(cmdOut[0],"rupert")
        self.assertEqual(cmdOut[1],"1000")
        self.assertEqual(cmdOut[3],"A9D31A2BB68D6C08133C86A425068A1F")
        self.assertEqual(cmdOut[4],"[U          ]")

        cmdOut = executeCmd("cat /etc/samba/smbpasswd|grep root")[0].split(':')
        self.assertEqual(cmdOut[0],"root")
        self.assertEqual(cmdOut[1],"0")
        self.assertEqual(cmdOut[3],"A9D31A2BB68D6C08133C86A425068A1F")
        self.assertEqual(cmdOut[4],"[U          ]")

        cmdOut = executeCmd("cat /etc/samba/smbusers|grep root")[0].split()
        self.assertEqual(cmdOut[0],"root")
        self.assertEqual(cmdOut[2],"administrator")

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
