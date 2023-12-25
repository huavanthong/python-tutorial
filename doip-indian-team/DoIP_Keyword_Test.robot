*** Variables ***
${config_file}     ./config/project-config.jsonp

*** Settings ***
Library    DoIPKeywordTest.py
Library      RobotFramework_TestsuitesManagement    WITH NAME    testsuites
# Suite Setup      testsuites.testsuite_setup
# Suite Teardown   testsuites.testsuite_teardown
# Test Setup       testsuites.testcase_setup
# Test Teardown    testsuites.testcase_teardown

*** Keywords ***
DOIP CSB Testing
   [arguments]  ${commands}
   [Documentation]  This test is the sanity test for DOIP
    [Tags]  DoIP
	[Teardown]   DoIP Disconnect
    DoIP Initialize
    Log to console  DoIP Initialize PASSED
    DoIP Start Tester Present  8  
    
    ${message}  DoIP Send Diag Message  1040
    ${message}  DoIP Send Diag Message  ${commands}

    DoIP Validate Diag Response  ${message}  0  3  7101
    DoIP Stop Tester Present
	Sleep  2

*** Test Cases ***
CSB Doip testcase 1 for reading tuner frequency table AM

   DOIP CSB Testing  31010E9B0A

CSB Doip testcase 2 for checking antena wiring harness Antena 2

   DOIP CSB Testing  31010E9802

CSB Doip testcase 3 for checking antena wiring harness Antena 3

   DOIP CSB Testing  31010E9803

CSB Doip testcase 4 for reading tuner frequency table DAB

   DOIP CSB Testing  31010E9B03

CSB Doip testcase 5 for reading tuner frequency table FM
   
   DOIP CSB Testing  31010E9B03


