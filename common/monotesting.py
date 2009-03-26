#################################################################
#
# Helper functions and framework for ASP.net testing 
# using Selenium and Testopia
#
# Author: Rusty Howell (rhowell@novell.com)
#

import sys,re
import unittest
import getopt
from testopia import Testopia

import creds
from defaults import *

#################################################################
#
# You must create two python modules (creds.py, defaults.py)
# 
# See the README for more information
#

xsp1_url = '%s:%s' % (base_url,xsp1_port)
xsp2_url = '%s:%s' % (base_url,xsp2_port)
graffiti_url = '%s:%s' % (base_url,graffiti_port)

# Testopia variables
mytestopia = None
testrun = None


#################################################################
#
# Local helper functions
#

value_args = {'base_url=':'URL of the webserver being tested',
        'testrunid=':'Test run id in Testopia',
        'xsp1_port=':'Port number that xsp1 is running on',
        'xsp2_port=':'Port number that xsp2 is running on',
        'graffiti_port=':'Port number that graffiti is running on',
        'rc_server=':'URL of the Selenium RC server',
        'rc_port=':'Port number that the RC server is using',
        'rc_browser=':'Browser that RC server should use',
        'showvalues':'Prints the current values',
        'help':'Prints this help message',
        'debug':'Prints debug messages (implies --showvalues)',
        'logfile=':'Write debug output to this file'}

#----------------------------------------------------------------------
def loadargs(cmdargs):
    global base_url,testrunid,xsp1_port,xsp2_port
    global rc_server,rc_port,rc_browser
    global graffiti_port, debug, logfile

    longargs = value_args.keys()
    shortargs = ''
    showvalues = False

    opts,args = getopt.getopt(cmdargs,shortargs,longargs)
    #print  opts
    #print args

    for o,a in opts:
        if o == '--base_url':
            base_url = a
        elif o == '--testrunid':
            if a == '': testrunid = None
            else: testrunid = int(a)
        elif o == '--xsp1_port':
            xsp1_port = int(a)
        elif o == '--xsp2_port':
            xsp2_port = int(a)
        elif o == '--graffiti_port':
            graffiti_port = int(a)

        elif o == '--rc_server':
            rc_server = a
        elif o == '--rc_port':
            rc_port = int(a)
        elif o == '--rc_browser':
            rc_browser = a
        elif o == '--showvalues':
            showvalues = True
        elif o == '--debug':
            debug = True
        elif o == '--logfile':
            print 'WARNING: --logfile is not yet implemented'
            logfile = None
        elif o == '--help':
            usage()
            sys.exit(0)

    if showvalues or debug:
        printValues()

#----------------------------------------------------------------------
def printValues():
    print "Current values:"
    print "base_url = %s" % base_url
    print "testrunid = %s" % str(testrunid)

    print "\nxsp1_port = %d" % xsp1_port
    print "xsp2_port = %d" % xsp2_port
    print "graffiti_port = %d" % graffiti_port

    print "\nrc_server = %s" % rc_server
    print "rc_port = %d" % rc_port
    print "rc_browser = %s\n" % rc_browser

    print "debug = %s" % debug
    print "logfile = %s\n" % logfile

#----------------------------------------------------------------------
def usage():
    print "\nUsage: %s [OPTIONS]\n" % sys.argv[0]

    for (k,v) in value_args.items():
        print '     ',
        print ('--'+ k).ljust(25),v.ljust(50)
    print ''

#----------------------------------------------------------------------
def log(msg):
    if debug:
        print msg

    if logfile != None:
        f = open(logfile,'a') # open using append
        f.write(msg)
        f.close()


####################################################################
#
#    main methods
#

def monotesting_main():
    loadargs(sys.argv[1:])
    sys.argv = sys.argv[:1]
    if debug:
        sys.argv.append('-v')
    unittest.main()

#----------------------------------------------------------------------

if __name__ == '__main__':
    print "Do not execute this module directly"
    sys.exit(1)
