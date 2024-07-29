*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${brower}     Firefox
${url}    https://demo.nopcommerce.com/


*** Test Cases ***
LoginTest
    Open Browser    ${url}    ${brower}
    loginToApplication
    close browser

*** Keywords ***
loginToApplication
    click link    xpath://a[@class='ico-login']
    input text     id:Email    pavanoltraining@gmail.com
    input text     id:Password    Test@123
    click element     xpath://button[contains(text(),'Log in')]