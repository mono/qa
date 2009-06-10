
import sys
import os
import unittest
import pdb

from defaults import *
from testopia import Testopia

creds_dir = os.path.join(os.environ['HOME'],'.bugzilla')
sys.path = [creds_dir] + sys.path
import creds
import monotesting as mono

BUG_STATUS = {'IDLE':1,
            'PASSED':2,
            'FAILED':3,
            'RUNNING':4,
            'PAUSED':5,
            'BLOCKED':6
            }
#####################################################################
#
#     Testopia helper functions
#

class monoTestCase(unittest.TestCase):
    mytestopia = None
    testCaseResults = {} # form of {'11111':'PASSED','222222':'FAILED'}
    errorMessages = {} # format {'111111':['Error message- blah blah','another error message'],'2222':[]}
    testcase_list = None

    def __init__(self,methodname="runTest"):
        unittest.TestCase.__init__(self,methodname)


    #----------------------------------------------------------------------
    def getTestopia(self):
        host='apibugzilla.novell.com'
        ssl=True
        #port=443
        port = None

        if monoTestCase.mytestopia == None:
            monoTestCase.mytestopia = Testopia(username=creds.username,password=creds.password,host=host,ssl=ssl,port=port)
        return monoTestCase.mytestopia

    #----------------------------------------------------------------------
    def getTestRun(self):
        testrun = None
        #log("Getting test run")
        if mono.testrunid == None or mono.testrunid == 0:
            #log("Warning: getTestRun(): testrunid == None")
            testrun = None
        elif testrun == None:
            testrun = self.getTestopia().testrun_get(mono.testrunid)
        return testrun


    #----------------------------------------------------------------------
    def isTestCaseInTestRun(self):
        if mono.testrunid == None:
            mono.log("Testrunid is None; isTestCaseInTestRun == true")
            return True

        if monoTestCase.testcase_list == None:
            mono.log("Calling Testopia API to get test case ids in test run")
            list = self.getTestopia().testrun_get_test_cases(mono.testrunid)
            monoTestCase.testcase_list = [tc['case_id'] for tc in list]

        if self.testcaseid in monoTestCase.testcase_list:
            mono.log("Testcase %s found in test run %s" % (self.testcaseid,mono.testrunid))
            return True

        # else add it to the test run
        mono.log("Testcase %s NOT found in test run %s" % (self.testcaseid,mono.testrunid))
        return False

    #----------------------------------------------------------------------
    def updateTestCase(self,errorsList):

        #pdb.set_trace()
        success = (len(errorsList) == 0)
        if success:
            self.__updateTestCase("PASSED")
        else:
            mono.log('errorsList = %s' % str(errorsList))
            self.__updateTestCase("FAILED",errorsList)

    #----------------------------------------------------------------------
    def passTestCase(self):
        self.__updateTestCase("PASSED")

    #----------------------------------------------------------------------
    def failTestCase(self,msg=None):
        self.__updateTestCase("FAILED",[msg])

    #----------------------------------------------------------------------
    def __updateTestCase(self,status,errorsList=None):
        # Added data to a static class dictionary and call testcase_update_batch at the end

        if self.testcaseid == None:
            mono.log("WARNING: __updateTestCase(): testcaseid == None; TESTOPIA WILL NOT BE UPDATED")
            return

        if self.getTestRun() == None:
            mono.log("WARNING: __updateTestCase(): getTestRun() returned None; TESTOPIA WILL NOT BE UPDATED")
            return

        mono.log("Adding test case #%d to the batch call" % self.testcaseid)
        monoTestCase.testCaseResults[self.testcaseid] = status

        if errorsList != None:
            for (i,e) in enumerate(errorsList):
                e = e.replace('\'','\"')
                msg = '''[%d]: %s''' % (i,e)
                monoTestCase.errorMessages[self.testcaseid].append(msg)
                #self.getTestopia().testcaserun_update_alt(
                #    tr['run_id'],
                #    self.testcaseid,
                #    tr['build_id'],
                #    tr['environment_id'],
                #    notes=msg)


def updateTestCaseBatch():
    '''Updates all the testcases with a single testopia.testcaserun_update(caserun_ids, case_run_status_id=None) call'''
    # testcase_update_batch(self, ids, values)

    mono.log("Updating Testopia with a batch call")

    sortedTests = {} # create a dictionary of lists
    for status in BUG_STATUS:
        sortedTests[status] = []

    for k,v in monoTestCase.testCaseResults.items():  # Sort test case results into the appropriate list
        for status in BUG_STATUS:
            if v == status:
                sortedTests[status].append(k) # Added key to this list

    for status in BUG_STATUS:  # make batch call for each possible status
        if len(sortedTests[status]) > 0:
            mono.log("   Making batch call for %s test cases" % (status))
            monoTestCase.mytestopia.testcaserun_update(sortedTests[status],BUG_STATUS[status])


    tr = monoTestCase.mytestopia.testrun_get(mono.testrunid)
    for testcaseid in monoTestCase.errorMessages:
        monoTestCase.errorMessages[testcaseid] = []
        mono.log("   Setting error messages for test case #%d",testcaseid)
        for msg in monoTestCase.errorMessages[testcaseid]:
            monoTestCase.mytestopia.testcaserun_update_alt(
                tr['run_id'],
                testcaseid,
                tr['build_id'],
                tr['environment_id'],
                notes=msg)

# vim:ts=4:expandtab:
