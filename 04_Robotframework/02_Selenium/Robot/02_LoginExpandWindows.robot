```
Keyword for learning:
- User Defined Keyword without Arguments
- User Defined Keyword with Arguments
- User Defined Keyword with Arguments & Return Value
```
*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}     http://www.newtours.demoaut.com/
${browser}    Firefox


*** Test Cases ***
TC1
    ${PageTitle}=    launchBrowser    ${url}    ${browser}
    Log To Console    ${PageTitle}
    Input Text    name:userName    mercury
    Input Text    name:password    mercury

*** Keywords ***
launchBrowser
    [Arguments]     ${appurl}    ${appbrowser}
    Open Browser    ${appurl}    ${appbrowser}
    # This keyword to expand the windows of brower
    Maximize Browser Window
    ${title}=    Get Title
    [Return]    ${title}