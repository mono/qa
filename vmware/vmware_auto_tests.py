#!/usr/bin/env python

import pdb
import subprocess
import unittest


class vmware_unit_tests(unittest.TestCase):
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
        cmdOut = self.__execute("zypper lr")[2:-1]

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

        #pdb.set_trace()
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
        #pdb.set_trace()
        self.assertEqual(cmdOut[0].strip(), "<html><body><p>Hello World!</p></body></html>")

if __name__ == "__main__":
    unittest.main()

# vim:ts=4:expandtab:
