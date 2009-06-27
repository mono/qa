#################################################################
#
# Helper functions and framework for ASP.net testing 
# using Selenium and Testopia
#
# Author: Rusty Howell (rhowell@novell.com)
#

import sys
import re
import os
import unittest
import getopt
import traceback
import getpass
import pdb
from time import time as clock
from testopia import Testopia

import ConfigParser

#################################################################
#
# You must create two python modules (creds.py, defaults.py)
# 
# See the README for more information
#


base_url = None
testrunid = None
xsp1_port = None
xsp2_port = None
xsp1_url = None
xsp2_url = None
graffiti_url = None
apache_url = None
rc_server = None
rc_port = None
rc_browser = None
graffiti_port = None
apache_port = None
verbose = None
logfile = None
usexsp2 = False
username = None
password = None


colors = {
        'norm':'\033[0m',
        'red':'\033[31m',
        'green':'\033[32m',
        'orange':'\033[33m',
        'blue':'\033[34m',
        'purple':'\033[35m',
        }

myTestopia = None
#################################################################
#
# Local helper functions
#

value_args = {'base_url=':'URL of the webserver being tested',
        'testrunid=':'Test run id in Testopia (use 0 or None to disable Testopia)',
        'xsp1_port=':'Port number that xsp1 is running on',
        'xsp2_port=':'Port number that xsp2 is running on',
        'graffiti_port=':'Port number that graffiti is running on',
        'apache_port=':'Port number that apache is running on',
        'rc_server=':'ip or dns of the Selenium RC server (do not prepend with \'http\')',
        'rc_port=':'Port number that the RC server is using',
        'rc_browser=':'Browser that RC server should use',
        'showvalues':'Prints the current values',
        'help':'Prints this help message',
        'verbose':'Prints debug messages (implies --showvalues)',
        'username=':'Username to login to Testopia',
        'password=':'Password to login to Testopia',
        'logfile=':'Write debug output to this file',
        'usexsp2':'Use xsp2 port'}

#----------------------------------------------------------------------
def __loadargs(cmdargs):
    global base_url,testrunid,xsp1_port,xsp2_port
    global xsp1_url,xsp2_url,graffiti_url,apache_url
    global rc_server,rc_port,rc_browser
    global graffiti_port, apache_port, verbose, logfile
    global usexsp2
    global username,password

    longargs = value_args.keys()
    shortargs = 'hvu:p:'
    showvalues = False

    opts,args = getopt.getopt(cmdargs,shortargs,longargs)
    #print  opts
    #print args

    for o,a in opts:
        if o == '--base_url':
            base_url = a
        elif o == '--testrunid':
            if a == '' or a == 'None' or a == '0':
                testrunid = None
            else:
                testrunid = int(a)
        elif o == '--xsp1_port':
            xsp1_port = int(a)
        elif o == '--xsp2_port':
            xsp2_port = int(a)
        elif o == '--graffiti_port':
            graffiti_port = int(a)
        elif o == '--apache_port':
            apache_port = int(a)
        elif o == '--rc_server':
            rc_server = a
        elif o == '--rc_port':
            rc_port = int(a)
        elif o == '--rc_browser':
            rc_browser = a
        elif o == '--showvalues':
            showvalues = True
        elif o in ('--verbose','-v'):
            verbose = True
        elif o == '--logfile':
            logfile = a
        elif o == '--usexsp2':
            usexsp2 = True
        elif o in ('--username','-u'):
            username = a
        elif o in ('--password','-p'):
            password = a
        elif o in ('--help','-h'):
            __usage()
            sys.exit(0)

        xsp1_url = "%s:%s" % (base_url,xsp1_port)
        xsp2_url = "%s:%s" % (base_url,xsp2_port)
        graffiti_url = "%s:%s" % (base_url,graffiti_port)
        apache_url = "%s:%s" % (base_url,apache_port)

    #pdb.set_trace()

    if showvalues or verbose:
        __printValues()

#----------------------------------------------------------------------
def __testTestopiaConn():
    '''mytestopia is set to None if the creds are invalid or if testrunid is None'''

    # TODO: better test to check if the test run is STOPPED?
    # That would check the creds and see if the test run could/should be modified.
    # That way we don't muck up our historical data

    global testrunid,myTestopia
    host='apibugzilla.novell.com'
    ssl=True
    port = None
    myTestopia = None

    if testrunid != None:
        print "Connecting to Testopia...",
        myTestopia = Testopia(username=username,password=password,host=host,ssl=ssl,port=port)
        version = myTestopia.testopia_api_version()
        if version == None:
            print "XMLRPC error: Check your credentials"
            myTestopia = None
        else:
            print "ok"
    if testrunid == None or myTestopia == None:
        print "Skipping Testopia syncing"

#----------------------------------------------------------------------
def __getCommonDir():
    '''Returns the absolute path of trunk/qa/common directory'''

    prefix = os.getcwd()
    for dir in  __file__.split('/')[:-1]: # this is the path of monotesting.py
        prefix = os.path.join(prefix,dir)
    return os.path.normpath(prefix)


#----------------------------------------------------------------------
def __loadConfFile():
    global base_url,testrunid,xsp1_port,xsp2_port
    global xsp1_url,xsp2_url,graffiti_url,apache_url
    global rc_server,rc_port,rc_browser
    global graffiti_port, apache_port, verbose,logfile
    global usexsp2

    conf_file = 'defaults.conf'
    conf_file_path = os.path.join(__getCommonDir(),conf_file)

    if not os.path.exists(conf_file_path):
        print "ERROR: Cannot find %s" % conf_file_path
        sys.exit(1)

    config = ConfigParser.ConfigParser()
    config.read(conf_file_path)

    # Required settings
    base_url = config.get('main','base_url')
    testrunid = config.get('main','testrunid')
    testrunid = __stringToIntOrNone(testrunid)

    xsp1_port = config.get('main','xsp1_port')
    xsp2_port = config.get('main','xsp2_port')
    graffiti_port = config.get('main','graffiti_port')
    apache_port = config.get('main','apache_port')

    rc_server = config.get('rc server','rc_server')
    rc_port = config.get('rc server','rc_port')
    rc_browser = config.get('rc server','rc_browser')

    #Optional settings
    if config.has_option('debug','verbose'):
        verbose = config.getboolean('debug','verbose')
    if config.has_option('debug','logfile'):
        logfile = config.get('debug','logfile')
        if logfile == 'None' or logfile == '':
            logfile = None


#----------------------------------------------------------------------
def __promptForCredentials():
    global username,password
    forcepwd = False
    if username == None or username == '': # username was passed in at commandline
        username = raw_input("Enter Testopia username: ")
        forcepwd = True # force pwd to be passed in on command line

    if password == None or password == '' or forcepwd: # pwd was not passed in or if user was passed in on cmdline
        password = getpass.getpass("Enter Testopia password for %s: " % username)

#----------------------------------------------------------------------
def __loadCredentials():
    '''Set the credentials for Testopia. If conf file non-existant, then
    prompt user for creds.'''

    global username,password
    if testrunid == None or testrunid == 0 or testrunid == '': #skip creds
        return

    # Otherwise, read the conf file
    creds_file = '.testopia_creds.conf'
    creds_file_path = os.path.join(os.environ['HOME'],creds_file)

    if not os.path.exists(creds_file_path) or username != None or username != '':
        __promptForCredentials()
    else: #read the conf file
        config = ConfigParser.ConfigParser()
        config.read(creds_file_path)

        if config.has_option('testopia','username'):
            username = config.get('testopia','username')
        if config.has_option('testopia','password'):
            password = config.get('testopia','password')
        if password == None or password == '' or username == None or username == '':
            __promptForCredentials()


#----------------------------------------------------------------------
def __stringToIntOrNone(s):
    if s == None or s == 'None' or s == '' or s == '0':
        return None
    else:
        return int(s)
#----------------------------------------------------------------------
def __setUrls():
    global xsp1_url,xsp2_url,graffiti_url,apache_url
    xsp1_url = '%s:%s' % (base_url,xsp1_port)
    xsp2_url = '%s:%s' % (base_url,xsp2_port)
    graffiti_url = '%s:%s' % (base_url,graffiti_port)
    apache_url = '%s:%s' % (base_url,apache_port)

#----------------------------------------------------------------------
def __printValues():
    print "Current values:"
    print "base_url = %s" % base_url
    print "testrunid = %s" % str(testrunid)

    print "\nxsp1_port = %s" % str(xsp1_port)
    print "xsp2_port = %s" % str(xsp2_port)
    print "graffiti_port = %s" % str(graffiti_port)
    print "apache_port = %s" % str(apache_port)

    print "\nrc_server = %s" % rc_server
    print "rc_port = %s" % str(rc_port)
    print "rc_browser = %s\n" % str(rc_browser)

    print "username = %s" % username
    print "verbose = %s" % verbose
    print "logfile = %s" % logfile
    print "usexsp2 = %s\n" % str(usexsp2)

#----------------------------------------------------------------------
def __usage():
    print "\nUsage: %s [OPTIONS]\n" % sys.argv[0]

    options = value_args.items()
    options.sort()

    for (k,v) in options:
        print '     ',
        print ('--'+ k).ljust(25),v.ljust(50)
    print ''

#----------------------------------------------------------------------
def log(msg):
    global logfile,verbose
    if verbose:
        print msg

    if logfile != None:
        f = open(logfile,'a') # open using append
        f.writelines(msg + '\n')
        f.close()

#----------------------------------------------------------------------
def __check_args():
    quit = False
    if base_url == '' or base_url == None:
        print "ERROR: base_url is not set"
        quit = True
    if xsp1_port == None or xsp1_port == 0:
        print "ERROR: xsp1_port is not set"
        quit = True
    if xsp2_port == None or xsp2_port == 0:
        print "ERROR: xsp2_port is not set"
        quit = True
    if graffiti_port == None or graffiti_port == 0:
        print "ERROR: graffiti_port is not set"
        quit = True
    if apache_port == None or apache_port == 0:
        print "ERROR: apache_port is not set"
        quit = True
    if rc_server == None or rc_server == '':
        print "ERROR: rc_server is not set"
        quit = True
    if rc_port == None or rc_port == 0:
        print "ERROR: rc_port is not set"
        quit = True
    if rc_browser == None or rc_browser == '':
        print "ERROR: rc_browser is not set"
        quit = True

    if quit:
        print "\nExiting\n"
        sys.exit(1)

#----------------------------------------------------------------------
def __flattenTestSuite(suite):
    '''This function takes a test suite and looks at each element which may
       be a test suite or a test case. If it's another test suite, it takes 
       test cases in it and adds it to the parent test suite.
    '''
    new_suite = unittest.TestSuite()
    for e in suite:
        if issubclass(e.__class__,unittest.TestSuite):
            new_e = __flattenTestSuite(e)
            new_suite.addTests(new_e)
        else:
            new_suite.addTest(e)
    return new_suite

#----------------------------------------------------------------------
def __printColor(msg,color):
    print '%s%s%s' % (colors[color],msg,colors['norm'])

####################################################################
#
#    main methods
#

def __runAllTests():

    loader = unittest.TestLoader()
    testsuite = loader.loadTestsFromModule(__import__('__main__'))

    print "\nRunning %d tests\n" % testsuite.countTestCases()
    #results = unittest.TextTestRunner(verbosity=2).run(testsuite)
    results = unittest.TestResult()

    testsuite = __flattenTestSuite(testsuite)
    totalCount = testsuite.countTestCases()
    skipped = 0

    for i,t in enumerate(testsuite):
        print "Running %d of %d: %s ..." % ( i+1, totalCount, t.id()),
        failures = len(results.failures)
        errors = len(results.errors)
        if t.isTestCaseInTestRun():
            t.run(results)
            if failures != len(results.failures): #Check if a failure was added
                __printColor("FAILED",'red')
            elif errors != len(results.errors):
                __printColor("ERROR",'red')
            else:
                print 'ok'
            # Get result from the results and print status
        else:
            __printColor("skipped [%d]" % t.testcaseid, 'orange')
            skipped += 1

    print "\n%12s:%3s" % ('Errors',len(results.errors))
    print "%12s:%3s" % ('Failures',len(results.failures))
    print "%12s:%3s" % ('Skipped',skipped)
    print "%12s:%3s" % ('Tests run',results.testsRun)
    print ''

    # All that ^^ just because unittest.main() calls sys.exit()

#----------------------------------------------------------------------
def monotesting_main(_usexsp2=False):
    args = sys.argv[1:]
    if _usexsp2:
        args += ['--usexsp2']
    __loadConfFile()
    __loadargs(args)
    __loadCredentials()
    __testTestopiaConn()
    __setUrls()
    __check_args()

    sys.argv = sys.argv[:1]
    if verbose:
        sys.argv.append('-v')

    start = clock()
    __runAllTests()

    etime = clock() - start
    print "Time: %dm %ds\n" % (etime / 60, etime % 60)


#----------------------------------------------------------------------

if __name__ == '__main__':
    print "Do not execute this module directly"
    sys.exit(1)

# vim:ts=4:expandtab:
