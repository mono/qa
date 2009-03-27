
import unittest

from defaults import *
from testopia import Testopia
import creds
from monotesting import *

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
        host='bugzilla.novell.com'
        ssl=True
        port=443

        if self.mytestopia == None:
            self.mytestopia = Testopia(username=creds.username,password=creds.password,host=host,ssl=ssl,port=port)
        return self.mytestopia

    #----------------------------------------------------------------------
    def getTestRun(self):
        global testrun
        log("Getting test run")
        if testrunid == None or testrunid == 0:
            log("Error: getTestRun(): testrunid == None")
            testrun = None
        elif testrun == None:
            testrun = self.getTestopia().testrun_get(testrunid)
        return testrun


    #----------------------------------------------------------------------
    def isTestCaseInTestRun(self):
        global testrunid
        if testrunid == None:
            log("Testrunid is None; isTestCaseInTestRun == true")
            return True

        list = self.getTestopia().testrun_get_test_cases(testrunid)
        testcase_list = [tc['case_id'] for tc in list]

        if self.testcaseid in testcase_list:
            log("Testcase %s found in test run %s" % (self.testcaseid,testrunid))
            return True
        
        log("Testcase %s NOT found in test run %s" % (self.testcaseid,testrunid))
        return False

    #----------------------------------------------------------------------
    def updateTestCase(self,errorsList):

        log(str(errorsList))
        success = (len(errorsList) == 0)
        if success:
            self.__updateTestCase("PASSED")
        else:
            print errorsList
            msg =''
            for (i,e) in enumerate(errorsList):
                msg += '''[%d]: %s''' % (i,e)
            self.__updateTestCase("FAILED",msg)

    #----------------------------------------------------------------------
    def passTestCase(self):
        self.__updateTestCase("PASSED")

    #----------------------------------------------------------------------
    def failTestCase(self,msg=None):
        self.__updateTestCase("FAILED",msg)

    #----------------------------------------------------------------------
    def __updateTestCase(self,status,msg=None):

        if self.testcaseid == None:
            log("Error: __updateTestCase(): testcaseid == None")
            return

        if self.getTestRun() == None:
            log("Error: __updateTestCase(): getTestRun() == None")
            return 

        log("   Setting testcase #%d status to %s" % (self.testcaseid,status))
        
        tr = self.getTestRun()
        self.getTestopia().testcaserun_update_alt(
                tr['run_id'],
                self.testcaseid,
                tr['build_id'],
                tr['environment_id'],
                case_run_status_id=BUG_STATUS[status],
                notes=msg)


# vim:ts=4:expandtab:
