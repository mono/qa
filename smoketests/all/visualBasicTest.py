#!/usr/bin/python

import sys,os
import unittest
import traceback
import subprocess
import uuid

filepath = os.path.realpath(__file__)
basepath = os.path.dirname(os.path.dirname(os.path.dirname(filepath)))
#basepath is the absolute path of the trunk/qa directory

sys.path.append(basepath)
import common.monotesting as mono
from common.helpers import *
from smoketests.smokeTestCase import smokeTestCase


####################################################################
#
#    xsp1TestCase class
#

class visualBasicTestCase(smokeTestCase):
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

        executeCmd('vbnc -out:helloworld_vb.exe helloworld.vb')
        out = executeCmd('mono helloworld_vb.exe')
        self.assertEqual(greeting,out[0].strip())


    def tearDown(self):
        self.remove('helloworld.vb')
        self.remove('helloworld_vb.exe')


if __name__ == '__main__':
    mono.monotesting_main()



# vim:ts=4:expandtab:
