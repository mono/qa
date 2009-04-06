
import unittest

from defaults import *
from testopia import Testopia
import creds
#from monotesting import *
import monotesting as mono
from monotesting import log

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

    def __init__(self,tmp):
        self.mytestopia = None
        unittest.TestCase.__init__(self,tmp)


    #----------------------------------------------------------------------
    def getTestopia(self):
        host='apibugzilla.novell.com'
        ssl=True
        #port=443
        port = None

        if self.mytestopia == None:
            self.mytestopia = Testopia(username=creds.username,password=creds.password,host=host,ssl=ssl,port=port)
        return self.mytestopia

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
        #global testrunid
        if mono.testrunid == None:
            log("Testrunid is None; isTestCaseInTestRun == true")
            return True

        list = self.getTestopia().testrun_get_test_cases(mono.testrunid)
        testcase_list = [tc['case_id'] for tc in list]

        if self.testcaseid in testcase_list:
            log("Testcase %s found in test run %s" % (self.testcaseid,mono.testrunid))
            return True
        
        log("Testcase %s NOT found in test run %s" % (self.testcaseid,mono.testrunid))
        return False

    #----------------------------------------------------------------------
    def updateTestCase(self,errorsList):

        log(str(errorsList))
        success = (len(errorsList) == 0)
        if success:
            self.__updateTestCase("PASSED")
        else:
            print errorsList
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
            log("WARNING: __updateTestCase(): testcaseid == None; TESTOPIA WILL NOT BE UPDATED")
            return

        if self.getTestRun() == None:
            log("WARNING: __updateTestCase(): getTestRun() returned None; TESTOPIA WILL NOT BE UPDATED")
            return 

        log("   Setting testcase #%d status to %s" % (self.testcaseid,status))
        
        tr = self.getTestRun()
        self.getTestopia().testcaserun_update_alt(
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
