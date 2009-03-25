#################################################################
#
# Helper functions and framework for ASP.net testing 
# using Selenium and Testopia
#
# Author: Rusty Howell (rhowell@novell.com)
#

import sys
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
        'help':'Prints this help message'}

#----------------------------------------------------------------------
def loadargs():
    global base_url,testrunid,xsp1_port,xsp2_port
    global rc_server,rc_port,rc_browser
    global graffiti_port

    longargs = value_args.keys()
    shortargs = ''

    opts,args = getopt.getopt(sys.argv[1:],shortargs,longargs)
    #print opts
    #print args

    for o,a in opts:
        if o == '--base_url':
            base_url = a
        elif o == '--testrunid':
            testrunid = int(a)
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
            printValues()
        elif o == '--help':
            usage()
            sys.exit(0)

#----------------------------------------------------------------------
def printValues():
    print "Current values:"
    print "base_url = %s" % base_url
    print "testrunid = %d" % testrunid

    print "\nxsp1_port = %d" % xsp1_port
    print "xsp2_port = %d" % xsp2_port
    print "graffiti_port = %d" % graffiti_port

    print "\nrc_server = %s" % rc_server
    print "rc_port = %d" % rc_port
    print "rc_browser = %s\n" % rc_browser

#----------------------------------------------------------------------
def usage():
    print "\nUsage: %s [OPTIONS]\n" % sys.argv[0]

    for (k,v) in value_args.items():
        print '     ',
        print ('--'+ k).ljust(25),v.ljust(50)
    print ''

#####################################################################
#
#     Testopia helper functions
#
BUG_STATUS = {'IDLE':1,
            'PASSED':2,
            'FAILED':3,
            'RUNNING':4,
            'PAUSED':5,
            'BLOCKED':6
            }

#----------------------------------------------------------------------
def getTestopia():
    global mytestopia

    host='bugzilla.novell.com'
    ssl=True
    port=443

    if mytestopia == None:
        mytestopia = Testopia(username=creds.username,password=creds.password,host=host,ssl=ssl,port=port)
    return mytestopia

#----------------------------------------------------------------------
def getTestRun():
    global testrun
    if testrunid == None or testrunid == 0:
        testrun = None
    elif testrun == None:
        testrun = getTestopia().testrun_get(testrunid)
    return testrun

#----------------------------------------------------------------------
def passTestCase(testcaseid):
    __updateTestCase(testcaseid,"PASSED")

#----------------------------------------------------------------------
def failTestCase(testcaseid):
    __updateTestCase(testcaseid,"FAILED")

#----------------------------------------------------------------------
def __updateTestCase(testcaseid,status):

    if testcaseid == None:
        return

    if getTestRun() == None:
        return 
    #print "Setting status to %s" % status
    
    tr = getTestRun()
    getTestopia().testcaserun_update_alt(
            tr['run_id'],
            testcaseid,
            tr['build_id'],
            tr['environment_id'],
            case_run_status_id=BUG_STATUS[status])

####################################################################
#
#    main methods
#

def monotesting_main():
    loadargs()
    sys.argv = sys.argv[:1]
    unittest.main()

#----------------------------------------------------------------------

if __name__ == '__main__':
    print "\nDo not call this module directly\n"
    sys.exit(1)

