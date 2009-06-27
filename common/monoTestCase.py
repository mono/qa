
import sys
import os
import unittest
import pdb

from testopia import Testopia
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
    testcase_list = None
    testrun = None

    def __init__(self,methodname="runTest"):
        unittest.TestCase.__init__(self,methodname)

    #----------------------------------------------------------------------
    def getTestRun(self):
        if mono.testrunid == None or mono.testrunid == 0 or mono.myTestopia == None:
            monoTestCase.testrun = None
        elif monoTestCase.testrun == None:
            monoTestCase.testrun = mono.myTestopia.testrun_get(mono.testrunid)
        return monoTestCase.testrun


    #----------------------------------------------------------------------
    def isTestCaseInTestRun(self):
        if mono.myTestopia == None:
            return True # return true so the test case is run, regardless of testopia

        if monoTestCase.testcase_list == None:
            mono.log("Getting test cases in test run")
            list = mono.myTestopia.testrun_get_test_cases(mono.testrunid)
            monoTestCase.testcase_list = [tc['case_id'] for tc in list]

        if self.testcaseid in monoTestCase.testcase_list:
            mono.log("Testcase %s found in test run %s" % (self.testcaseid,mono.testrunid))
            return True
        #else:
        #    mono.log("Adding test case %s to test run %s" % (self.testcaseid,mono.testrunid))
        #    self.getTestopia().testcase_add_to_run(self.testcaseid, mono.testrunid)

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

        if self.testcaseid == None:
            mono.log("WARNING: __updateTestCase(): testcaseid == None; TESTOPIA WILL NOT BE UPDATED")
            return

        tr = self.getTestRun()
        if tr == None:
            mono.log("WARNING: __updateTestCase(): getTestRun() returned None; TESTOPIA WILL NOT BE UPDATED")
            return

        mono.log("   Setting testcase #%d status to %s" % (self.testcaseid,status))
        
        mono.myTestopia.testcaserun_update_alt(
                tr['run_id'],
                self.testcaseid,
                tr['build_id'],
                tr['environment_id'],
                case_run_status_id=BUG_STATUS[status])

        if errorsList != None:
            for (i,e) in enumerate(errorsList):
                e = e.replace('\'','\"')
                msg = '''[%d]: %s''' % (i,e)
                self.getTestopia().testcaserun_update_alt(
                    tr['run_id'],
                    self.testcaseid,
                    tr['build_id'],
                    tr['environment_id'],
                    notes=msg)



# vim:ts=4:expandtab:
