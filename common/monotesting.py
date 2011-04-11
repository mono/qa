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

from monoTestopia import monoTestopia as Testopia
import helpers

import ConfigParser
import monoTestRunner

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
xsp4_port = None
xsp1_url = None
xsp2_url = None
xsp4_url = None
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
usexsp4 = False
username = None
password = None
failed = False
config = None

###############################################################
# Testopia connection info
testopia_url = 'apibugzilla.novell.com'
testopia_ssl = True
testopia_port = None


#################################################################
#
# Local helper functions
#

value_args = {
        'base_url=':'URL of the webserver being tested',
        'testrunid=':'Test run id in Testopia (use 0 or None to disable Testopia)',
        'xsp1_port=':'Port number that xsp1 is running on',
        'xsp2_port=':'Port number that xsp2 is running on',
        'xsp4_port=':'Port number that xsp4 is running on',
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
        'usexsp2':'Use xsp2 port',
        'usexsp4':'Use xsp4 port',
        'failed':'Only run failed tests',
}

#----------------------------------------------------------------------
def __loadargs(cmdargs):
    global base_url,testrunid,xsp1_port,xsp2_port,xsp4_port
    global xsp1_url,xsp2_url,xsp4_url,graffiti_url,apache_url
    global rc_server,rc_port,rc_browser
    global graffiti_port, apache_port, verbose, logfile
    global usexsp2,usexsp4
    global username,password,failed
    global message

    longargs = value_args.keys()
    shortargs = 'hvu:p:'
    showvalues = False

    opts,args = getopt.getopt(cmdargs,shortargs,longargs)
    #print opts
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
        elif o == '--xsp4_port':
            xsp4_port = int(a)
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
        elif o == '--usexsp4':
            usexsp4 = True
        elif o in ('--username','-u'):
            username = a
        elif o in ('--password','-p'):
            password = a
        elif o in ('--help','-h'):
            __usage()
            sys.exit(0)
        elif o == '--failed':
            failed = True

        xsp1_url = "%s:%s" % (base_url,xsp1_port)
        xsp2_url = "%s:%s" % (base_url,xsp2_port)
        xsp4_url = "%s:%s" % (base_url,xsp4_port)
        graffiti_url = "%s:%s" % (base_url,graffiti_port)
        apache_url = "%s:%s" % (base_url,apache_port)


    if showvalues or verbose:
        __printValues()

#----------------------------------------------------------------------
def __testTestopiaConn():
    #global myTestopia
    helpers.myTestopia = Testopia(username=username,password=password,host=testopia_url,ssl=testopia_ssl,testrunid=testrunid)
    helpers.myTestopia.testConnection()

#----------------------------------------------------------------------
def __getCommonDir():
    '''Returns the absolute path of trunk/qa/common directory'''

    dir = os.path.join(os.getcwd(),os.path.dirname(__file__))
    return os.path.normpath(dir)


#----------------------------------------------------------------------
def __loadConfigOption(option):
    value = None
    if config.has_option('main',option):    # config file has only 'main'
        value = config.get('main',option)
    return value

#----------------------------------------------------------------------
def __loadConfFile():
    global base_url,testrunid,xsp1_port,xsp2_port,xsp4_port
    global xsp1_url,xsp2_url,xsp4_url,graffiti_url,apache_url
    global rc_server,rc_port,rc_browser
    global graffiti_port, apache_port, verbose,logfile
    global usexsp2,usexsp4,config

    conf_file = 'defaults.conf'
    conf_file_path = os.path.join(__getCommonDir(),conf_file)

    if not os.path.exists(conf_file_path):
        helpers.printColor("Warning: Cannot find conf file '%s'" % conf_file_path,'red')
        return

    config = ConfigParser.ConfigParser()
    config.read(conf_file_path)

    # Required settings
    base_url = __loadConfigOption('base_url')
    testrunid = __loadConfigOption('testrunid')
    testrunid = __stringToIntOrNone(testrunid)

    xsp1_port = __loadConfigOption('xsp1_port')
    xsp2_port = __loadConfigOption('xsp2_port')
    xsp4_port = __loadConfigOption('xsp4_port')
    graffiti_port = __loadConfigOption('graffiti_port')
    apache_port = __loadConfigOption('apache_port')

    rc_server = __loadConfigOption('rc_server')
    rc_port = __loadConfigOption('rc_port')
    rc_browser = __loadConfigOption('rc_browser')

    #Optional settings
    if config.has_option('main','verbose'):
        verbose = config.getboolean('main','verbose')
    logfile = __loadConfigOption('logfile')
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

    #pdb.set_trace()
    # Otherwise, read the conf file
    creds_file = '.testopia_creds.conf'
    creds_file_path = os.path.join(os.environ['HOME'],creds_file)

    if not os.path.exists(creds_file_path) or (username != None and username != ''):
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
    global xsp1_url,xsp2_url,xsp4_url,graffiti_url,apache_url
    xsp1_url = '%s:%s' % (base_url,xsp1_port)
    xsp2_url = '%s:%s' % (base_url,xsp2_port)
    xsp4_url = '%s:%s' % (base_url,xsp4_port)
    graffiti_url = '%s:%s' % (base_url,graffiti_port)
    apache_url = '%s:%s' % (base_url,apache_port)

#----------------------------------------------------------------------
def __printValues():
    print "Current values:"
    print "base_url = %s" % base_url
    print "testrunid = %s" % str(testrunid)
    print "\n"
    print "xsp1_port = %s" % str(xsp1_port)
    print "xsp2_port = %s" % str(xsp2_port)
    print "xsp4_port = %s" % str(xsp4_port)
    print "graffiti_port = %s" % str(graffiti_port)
    print "apache_port = %s" % str(apache_port)
    print "\n"
    print "rc_server = %s" % rc_server
    print "rc_port = %s" % str(rc_port)
    print "rc_browser = %s" % str(rc_browser)
    print "\n"
    print "username = %s" % username
    print "verbose = %s" % verbose
    print "logfile = %s" % logfile
    print "usexsp2 = %s" % str(usexsp2)
    print "usexsp4 = %s" % str(usexsp4)
    print "\n"

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

####################################################################
#
#    main methods
#

def monotesting_main(_usexsp2=False, _usexsp4=False):
    args = sys.argv[1:]
    if _usexsp2:
        args += ['--usexsp2']
    if _usexsp4:
        args += ['--usexsp4']
    __loadConfFile()
    __loadargs(args)
    __loadCredentials()
    start = clock()
    __testTestopiaConn()
    __setUrls()

    sys.argv = sys.argv[:1]
    if verbose:
        sys.argv.append('-v')

    runner = monoTestRunner.monoTestRunner(runFailedOnly=failed)
    results = runner.runAllTests()

    helpers.myTestopia.updateAllTestCases(results)

    etime = clock() - start
    print "\nTime: %dh %dm %ds\n" % (etime / 3600, (etime % 3600) / 60, etime % 60)

    #print 'API calls: %d\n' % myTestopia.apicalls


#----------------------------------------------------------------------

if __name__ == '__main__':
    print "Do not execute this module directly"
    sys.exit(1)

# vim:ts=4:expandtab:
