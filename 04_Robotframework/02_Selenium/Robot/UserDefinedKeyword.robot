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
${browser}    chrome


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
    Maximize Browser Window
    ${title}=    Get Title
    [Return]    ${title}