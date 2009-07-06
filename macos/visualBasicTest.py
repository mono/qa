#!/usr/bin/python

import sys,os
import unittest
import traceback
import subprocess

filepath = os.path.realpath(__file__)
basepath = os.path.dirname(os.path.dirname(filepath))
#basepath is the absolute path of the trunk/qa directory

sys.path.append(basepath)


import common.monotesting as mono
from common.monoTestCase import monoTestCase


####################################################################
#
#    xsp1TestCase class
#

class visualBasicTestCase(monoTestCase):
    testcaseid = 0

    def test(self):
        code = '''
Public Class m
   Public Shared Sub Main()
     System.Console.WriteLine("hello")
   End Sub
End Class
'''

        f = open('helloworld.vb','w')
        f.write(code)
        f.close()

        proc1= subprocess.Popen('vbnc -out:main.exe helloworld.vb',shell=True)
        proc1.wait()

        proc2= subprocess.Popen('mono main.exe',shell=True,stdout=subprocess.PIPE)
        proc2.wait()

        out = proc2.stdout.readlines()
        self.assertEqual('hello',out[0].strip())


    


if __name__ == '__main__':
    mono.monotesting_main()



# vim:ts=4:expandtab:
