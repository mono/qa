

import unittest
import pdb
import monotesting as mono

colors = {
        'norm':'\033[0m',
        'red':'\033[31m',
        'green':'\033[32m',
        'orange':'\033[33m',
        'blue':'\033[34m',
        'purple':'\033[35m',
}

#----------------------------------------------------------------------
def __flattenTestSuite(suite):
    '''This function takes a test suite and looks at each element which may
       be a test suite or a test case. If it's another test suite, it takes#
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

#----------------------------------------------------------------------

def runAllTests():
    '''Runs the tests are returns a dict of lists of passed and failed tests '''
    d = {'passed':[],'failed':[],'errors':[]}

    loader = unittest.TestLoader()
    testsuite = loader.loadTestsFromModule(__import__('__main__'))

    print "\nRunning %d tests\n" % testsuite.countTestCases()
    results = unittest.TestResult()

    testsuite = __flattenTestSuite(testsuite)
    totalCount = testsuite.countTestCases()
    skipped = 0

    try:
        for i,t in enumerate(testsuite):
            print "Running %d of %d: %s ..." % ( i+1, totalCount, t.id()),
            failures = len(results.failures)
            errors = len(results.errors)
            if t.isTestCaseInTestRun():
                t.run(results)
                if failures != len(results.failures): #Check if a failure was added
                    __printColor("FAILED",'red')
                    d['failed'].append(t.testcaseid)
                elif errors != len(results.errors):
                    __printColor("ERROR",'red')
                    d['errors'].append(t.testcaseid)
                else:
                    print 'ok'
                    d['passed'].append(t.testcaseid)
            # Get result from the results and print status
            else:
                __printColor("skipped [%d]" % t.testcaseid, 'orange')
                skipped += 1
    except KeyboardInterrupt:
        print "\n ** Aborting test run **"

    if len(results.errors) > 0:
        print '-' * 80
        print '   ERRORS'
        for e in results.errors:
            print e[1]

    if len(results.failures) > 0:
        print '-' * 80
        print '   FAILURES'
        for f in results.failures:
            print f[1]

    print "\n%12s:%3s" % ('Errors',len(results.errors))
    print "%12s:%3s" % ('Failures',len(results.failures))
    print "%12s:%3s" % ('Skipped',skipped)
    print "%12s:%3s\n" % ('Tests run',results.testsRun)

    return d

    # All that ^^ just because unittest.main() calls sys.exit()

# vim:ts=4:expandtab:
