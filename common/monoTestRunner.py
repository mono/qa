

import unittest
import sys
import pdb

import helpers


class monoTestRunner():
    def __init__(self,runFailedOnly = False):
        self.runFailedOnly = runFailedOnly

    #----------------------------------------------------------------------
    def __flattenTestSuite(self,suite):
        '''This function takes a test suite and looks at each element which may
           be a test suite or a test case. If it's another test suite, it takes#
           test cases in it and adds it to the parent test suite.
        '''
        new_suite = unittest.TestSuite()
        for e in suite:
            if issubclass(e.__class__,unittest.TestSuite):
                new_e = self.__flattenTestSuite(e)
                new_suite.addTests(new_e)
            else:
                new_suite.addTest(e)
        return new_suite

    #----------------------------------------------------------------------
    def filterForFailedTestCases(self,testsuite):
        print "Re-running FAILED test cases:"
        newsuite = unittest.TestSuite()
        for t in testsuite:
            if helpers.myTestopia.hasTestCaseFailed(t.testcaseid):
                print "    %s" % t.__class__.__name__
                newsuite.addTest(t)
        return newsuite

    #----------------------------------------------------------------------
    def setTestCasesToRunning(self,testsuite):
        print "Setting test cases to running"

        ids = []
        for t in testsuite:
            ids.append(t.testcaseid)
        runningIds = helpers.myTestopia.filterTestCasesInRun(ids=ids)
        helpers.myTestopia.updateTestCasesList(ids=runningIds,status='running')


    #----------------------------------------------------------------------
    def runAllTests(self):
        '''Runs the tests are returns a dict of lists of passed and failed tests '''
        aborted = False
        errors = {} # {testcaseid,[list of errors]}

        loader = unittest.TestLoader()
        testsuite = loader.loadTestsFromModule(__import__('__main__'))
        d = {'passed':[],'failed':[],'errors':[]}

        testsuite = self.__flattenTestSuite(testsuite)
        if self.runFailedOnly:
            testsuite = self.filterForFailedTestCases(testsuite)

        self.setTestCasesToRunning(testsuite)

        print "\nRunning %d tests\n" % testsuite.countTestCases()
        totalCount = testsuite.countTestCases()
        results = unittest.TestResult()
        skipped = 0

        try:
            for i,t in enumerate(testsuite):
                print "Running %d of %d: %s ..." % ( i+1, totalCount, t.id()),
                sys.stdout.flush()
                failures = len(results.failures)
                errors = len(results.errors)
                #status = ''
                if helpers.myTestopia.isTestCaseInTestRun(t.testcaseid):
                    t.run(results)
                    if failures != len(results.failures): #Check if a failure was added
                        helpers.printColor("FAILED",'red')
                        d['failed'].append(t.testcaseid)
                        #status = 'failed'
                        d[t.testcaseid] = t.verificationErrors
                        print results.failures[-1][1] # print the stack trace
                    elif errors != len(results.errors):
                        helpers.printColor("ERROR",'red')
                        d['errors'].append(t.testcaseid)
                        #status = 'failed'
                        d[t.testcaseid] = t.verificationErrors
                        print results.errors[-1][1] # print the stack trace
                    else:
                        print 'ok'
                        d['passed'].append(t.testcaseid)
                        #status = 'passed'

                    #helpers.myTestopia.updateTestCaseViaThread(testcaseid=t.testcaseid,status=status,errorsList=t.verificationErrors)
                    #print "done"

                # Get result from the results and print status
                else:
                    helpers.printColor("skipped [%d]" % t.testcaseid, 'orange')
                    skipped += 1
        except KeyboardInterrupt:
            # The interrupted test run is counted as 'run' ie. 'passed'
            print "\n ** Aborting test run. Testopia will not be updated **"
            aborted = True

        resFailures = len(results.failures)
        resErrors = len(results.errors)
        resPassed = results.testsRun - (resFailures + resErrors)

        print "\n%12s:%3s" % ('Passed',resPassed)
        print "%12s:%3s" % ('Errors',resErrors)
        print "%12s:%3s" % ('Failures',resFailures)
        print "%12s:%3s" % ('Skipped',skipped)
        print "%12s:%3s\n" % ('Tests run',results.testsRun)


        return d

        # All that ^^ just because unittest.main() calls sys.exit()

if __name__ == '__main__':
    print "Do not run this module directly"
    sys.exit(1)

# vim:ts=4:expandtab:
