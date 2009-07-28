#!/usr/bin/env python

import sys
import os
import unittest
import traceback
import subprocess
import uuid
import tempfile

basepath = os.path.dirname(os.path.realpath(__file__))
while not os.path.isfile(os.path.join(basepath,'common','monoTestCase.py')):
    basepath = os.path.dirname(basepath)
if not basepath in sys.path:
    sys.path.append(basepath)

import common.monotesting as mono
from smoketests.smokeTestCase import smokeTestCase
from common.helpers import *


####################################################################
#
#    gmcs2TestCase class
#

class gmcs2TestCase(smokeTestCase):
    testcaseid = 875239

    def setUp(self):
        self.tmpDir = tempfile.mkdtemp()
        self.startDir = os.getcwd()
        os.chdir(self.tmpDir)

    def test(self):
        u = uuid.uuid1()
        greeting = "Hello World %s" % u.hex # Generate a unique Hello world greeting
        code = '''
using System;
using System.Collections.Generic;
using System.IO;
using System.Net;

class m
{
    public static void Main(){
        List<string> l = new List<string>();
        l.Add("%s");

        foreach (string s in l)
        {
            Console.WriteLine(s);
        }
    }
}
''' % greeting

        f = open('list.cs','w')
        f.write(code)
        f.close()

        executeCmd('gmcs -out:list_cs.exe list.cs')
        out = executeCmd('mono list_cs.exe')
        self.assertEqual(greeting,out[0].strip())

    def tearDown(self):
        self.remove('list.cs')
        self.remove('list_cs.exe')
        os.chdir(self.startDir)
        os.rmdir(self.tmpDir)


if __name__ == '__main__':
    mono.monotesting_main()



# vim:ts=4:expandtab:
