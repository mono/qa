#!/usr/bin/python

import sys,os
import unittest
import traceback
import subprocess
import uuid

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
        u = uuid.uuid1()
        greeting = "Hello World %s" % u.hex # Generate a unique Hello world greeting
        code = '''
Public Class m
   Public Shared Sub Main()
     System.Console.WriteLine("%s")
   End Sub
End Class
''' % greeting

        f = open('helloworld.vb','w')
        f.write(code)
        f.close()

        proc1= subprocess.Popen('vbnc -out:main.exe helloworld.vb',shell=True,stdout=subprocess.PIPE)
        proc1.wait()

        proc2= subprocess.Popen('mono main.exe',shell=True,stdout=subprocess.PIPE)
        proc2.wait()

        out = proc2.stdout.readlines()
        self.assertEqual(greeting,out[0].strip())


    


if __name__ == '__main__':
    mono.monotesting_main()



# vim:ts=4:expandtab:
