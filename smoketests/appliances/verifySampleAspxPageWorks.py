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


class verifySampleAspxPageWorks(smokeTestCase):
    testcaseid = 816722

    def test(self):
        cmdOut = executeCmd("export TSTSTR=tc816722-$(uuidgen) ;" +
                            "export WEBDIR=/srv/www/htdocs/$TSTSTR ;" +
                            "export TMPDIR=/tmp/$TSTSTR ;" +
                            "mkdir -p $WEBDIR ;" +
                            "echo '<html><body><p><%= \"Hello World!\" %></p></body></html>' > $WEBDIR/index.aspx ;" +
                            "mkdir -p $TMPDIR ;" +
                            "cd $TMPDIR ;" +
                            "wget http://localhost/$TSTSTR > /dev/null 2>&1 ;"+
                            "cat index.html ;" +
                            "rm -rf $WEBDIR ;" +
                            "rm -rf $TMPDIR")
        self.assertEqual(cmdOut[0].strip(), "<html><body><p>Hello World!</p></body></html>")

if __name__ == "__main__":
    mono.monotesting_main()

# vim:ts=4:expandtab:
