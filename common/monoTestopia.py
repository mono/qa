#################################################################
#
# Helper functions for Testopia calls
#
# Author: Rusty Howell (rhowell@novell.com)
#

from testopia import Testopia
import types
from threading import Thread

BUG_STATUS = {'IDLE':1,
            'PASSED':2,
            'FAILED':3,
            'RUNNING':4,
            'PAUSED':5,
            'BLOCKED':6
            }

myTestopia = None
#--------------------------------------------------------------------------------------
class monoTestopiaThread(Thread):
    def __init__(self,myTestopia,testcaseid,status,errorsList=None):
        Thread.__init__(self)
        self.myTestopia = myTestopia
        self.testcaseid = testcaseid
        self.status = status.upper()
        self.errorsList = errorsList

    def run(self):
        tr = self.myTestopia.testrun
        #print "THREAD %d: updating Testopia" % self.testcaseid

        if self.errorsList == None or len(self.errorsList) == 0:
            self.myTestopia.testcaserun_update_alt(
                    run_id=tr['run_id'],
                    case_id=self.testcaseid,
                    build_id=tr['build_id'],
                    environment_id=tr['environment_id'],
                    case_run_status_id=BUG_STATUS[self.status])
        else:
            for (i,e) in enumerate(self.errorsList):
                e = e.replace('\'','\"')
                msg = '''[%d]: %s''' % (i,e)
                self.myTestopia.testcaserun_update_alt(
                    run_id=tr['run_id'],
                    case_id=self.testcaseid,
                    build_id=tr['build_id'],
                    environment_id=tr['environment_id'],
                    case_run_status_id=BUG_STATUS[self.status],
                    notes=msg)
        #print "THREAD %d: finished" % self.testcaseid


#--------------------------------------------------------------------------------------

class monoTestopia(Testopia):
    def __init__(self,username,password,host,ssl,testrunid):
        Testopia.__init__(self,username=username,password=password,host=host,ssl=ssl)
        self.testrunid = testrunid
        self.testcaseids = None
        self.failed_testcaseids = None
        self.testrun = None

        self.canConnect = False
        self.apicalls = 0
        self.threadlist = []

    #--------------------------------------------------------------------------------
    def __getData(self):
        self.testrun = self.testrun_get(self.testrunid)
        self.testcaseruns = self.testrun_get_test_case_runs(self.testrunid)
        self.apicalls += 2

        self.testcaseids = [tcr['case_id'] for tcr in self.testcaseruns]
        self.failed_testcaseids = [tcr['case_id'] for tcr in self.testcaseruns if tcr['case_run_status_id'] == 3]
        self.testcaseruns_hash = {}
        for tcr in self.testcaseruns:
            self.testcaseruns_hash[tcr['case_id']] = tcr['case_run_id']
        #print self.testcaseruns_hash

    #--------------------------------------------------------------------------------
    def __convertToTestCaseRunIds(self,testcaseids):
        '''Converts a list of testcaseids to the corresponding testcaserunids'''
        return [self.testcaseruns_hash[tcid] for tcid in testcaseids]

    #--------------------------------------------------------------------------------
    def testConnection(self):
        '''mytestopia is set to None if the creds are invalid or if testrunid is None'''

        # TODO: better test to check if the test run is STOPPED?
        # That would check the creds and see if the test run could/should be modified.
        # That way we don't muck up our historical data

        if self.testrunid != None:
            print "\nConnecting to Testopia...",
            version = self.testopia_api_version()
            self.apicalls += 1
            if version == None:
                print "XMLRPC error: Check your credentials"
                self.canConnect = False
            else:
                print "ok"
                self.canConnect = True
                self.__getData()
        else:
            self.canConnect = False
        if self.testrunid == None or self.canConnect == False:
            print "Skipping Testopia syncing"

    #--------------------------------------------------------------------------------
    def filterTestCasesInRun(self,ids):
        '''This takes a list of possible testcases and filters out any that
            are not in the testrun. Akin to isTestCaseInTestRun but for multiple ids'''
        newids = []
        if self.canConnect:
            for id in ids:
                if id in self.testcaseids:
                    newids.append(id)
        else:
            newids = ids
        return newids


    #--------------------------------------------------------------------------------
    def isTestCaseInTestRun(self,testcaseid):
        '''Returns true if the test case is in the test run'''

        if not self.canConnect:
            return True # return true so the test case is run, regardless of testopia

        return testcaseid in self.testcaseids

    #--------------------------------------------------------------------------------
    def addTestCaseToRun(self,testcaseid):
        pass

    #--------------------------------------------------------------------------------
    def hasTestCaseFailed(self,testcaseid):
        if not self.canConnect:
            return True # return true so the test case is run, regardless of testopia

        return testcaseid in self.failed_testcaseids

    #--------------------------------------------------------------------------------
    def updateTestCasesList(self,ids,status):
        if self.canConnect:
            status = status.upper()
            print "Updating %d %s test cases" % (len(ids),status)
            caserun_ids = self.__convertToTestCaseRunIds(ids)
            self.testcaserun_update(caserun_ids=caserun_ids,case_run_status_id=BUG_STATUS[status])
        #else:
        #    print "Cannot update %d %s test cases" % (len(ids),status)

    #--------------------------------------------------------------------------------
    def updateAllTestCases(self,results):
        if not self.canConnect:
            return
        # results = {'failed': [], 'errors': [], 'passed': [837262, 426296]}
        tresults = {'passed':results['passed'],'failed':results['failed'].extend(results['errors'])}

        if len(results['passed']) > 0:
            self.updateTestCasesList(results['passed'],'PASSED')

        for key in results.keys():
            if type(key) is int:
                self.updateTestCase(key,'FAILED',errorsList=results[key])              

    #--------------------------------------------------------------------------------
    def updateTestCase(self,testcaseid,status,errorsList=None):
        if not self.canConnect:
            return
        print "Updating failed test case %d" % testcaseid

        tr = self.testrun

        if errorsList == None or len(errorsList) == 0:
            self.testcaserun_update_alt(
                    run_id=tr['run_id'],
                    case_id=testcaseid,
                    build_id=tr['build_id'],
                    environment_id=tr['environment_id'],
                    case_run_status_id=BUG_STATUS[status])
            self.apicalls += 1
        else:
            for (i,e) in enumerate(errorsList):
                e = e.replace('\'','\"')
                msg = '''[%d]: %s''' % (i,e)
                self.testcaserun_update_alt(
                    run_id=tr['run_id'],
                    case_id=testcaseid,
                    build_id=tr['build_id'],
                    environment_id=tr['environment_id'],
                    case_run_status_id=BUG_STATUS[status],
                    notes=msg)

                self.apicalls += 1

    #--------------------------------------------------------------------------------
    def updateTestCaseViaThread(self,testcaseid,status,errorsList=None):
        if self.canConnect:
            curthread = monoTestopiaThread(self,testcaseid,status,errorsList=errorsList)
            self.threadlist.append(curthread)
            curthread.start()

    def waitForThreads(self):
        for curthread in self.threadlist:
            curthread.join()



#--------------------------------------------------------------------------------

# vim:ts=4:expandtab:
