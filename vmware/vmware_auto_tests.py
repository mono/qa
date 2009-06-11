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

    def testZypperRefreshes(self):
        # Testcase 546312
        cmdOut = self.__execute("zypper lr")[2:-1]
        for curRefresh in cmdOut:
            self.assertEqual(curRefresh.split()[-1], "No")

    def testMonoStableRepoUrl(self):
        # Testcase 546327
        cmdOut = self.__execute("zypper lr -u")[2:-1]
        hasMonoStableRepo = False
        #pdb.set_trace()
        for curLine in cmdOut:
            if curLine.split()[2] == "mono-stable-11.1":
                hasMonoStableRepo = True
                self.assertEqual(curLine.split()[-1], "http://ftp.novell.com/pub/mono/download-stable/openSUSE_11.1/")
        self.assertTrue(hasMonoStableRepo)

    def testDiskSize(self):
        # Testcase 546325
        cmdOut = self.__execute("df -h")
        diskSize = cmdOut[1].split()[1]
        self.assertEqual(diskSize, "30G")



if __name__ == "__main__":
    unittest.main()

# vim:ts=4:expandtab:
