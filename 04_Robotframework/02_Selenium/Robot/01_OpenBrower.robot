*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${HOMEPAGE}     http://www.google.com
${BROWSER}      Firefox

*** Keywords ***
Open the browser
    Open Browser    ${HOMEPAGE}    ${BROWSER}

Search topic
    [Arguments]    ${topic}
    Input Text    name=q    ${topic}
    Press Key    name=q    \\13

*** Test Cases ***
Open Browser Firefox
    Open the browser

Search on Google
    [Setup]    Open the browser
    Search topic    browserstack

Open Browser Edge
    Open Browser     http://www.google.com    Edge

Open Browser Edge then Search
    Open Browser     http://www.google.com    Edge
    Search topic     browserstack