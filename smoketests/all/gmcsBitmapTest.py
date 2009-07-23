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
from smoketests.smokeTestCase import smokeTestCase
from common.helpers import *


####################################################################
#
#    xsp1TestCase class
#

class gmcs2TestCase(smokeTestCase):
    testcaseid = 0
    codefile = 'bitmap.cs'
    exefile = 'bitmap_test.exe'

    def test(self):
        u = uuid.uuid1()
        greeting = "Hello World %s" % u.hex # Generate a unique Hello world greeting
        code = '''
using System;
using System.Drawing;
using System.Drawing.Imaging;

public class mclass 
{
    public static void Main()
    {
        Bitmap image = new Bitmap(100,100);
        Console.WriteLine("%s");

    }
}

''' % greeting

        f = open(self.codefile,'w')
        f.write(code)
        f.close()

        executeCmd('gmcs -out:%s %s -r:System.Drawing.dll' % (self.exefile,self.codefile))
        out = executeCmd('mono %s' % self.exefile)
        self.assertEqual(greeting,out[0].strip())

    def tearDown(self):
        self.remove(self.codefile)
        self.remove(self.exefile)


if __name__ == '__main__':
    mono.monotesting_main()



# vim:ts=4:expandtab:
