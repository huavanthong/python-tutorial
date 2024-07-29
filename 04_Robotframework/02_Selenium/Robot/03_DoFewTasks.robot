*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Add Tasks And Set To Complete
    Open Browser    url=https://todomvc.com/examples/angularjs/#/    browser=Firefox
    Input Text    class:new-todo    Complete Robot Framework Training
    Press Keys    class:new-todo    RETURN
    Input Text    class:new-todo    Write Automated Tests
    Press Keys    class:new-todo    RETURN
    Input Text    class:new-todo    Take a nap
    Press Keys    class:new-todo    RETURN
    Element Text Should Be    class:todo-count    3 items left
    Click Element    xpath: //*[contains(text(), "Complete Robot Framework Training")]/../input
    Element Text Should Be    class:todo-count    2 items left
    Click Element    xpath: //*[contains(text(), "Write Automated Tests")]/../input
    Element Text Should Be    class:todo-count    1 item left
    Click Element    xpath: //*[contains(text(), "Take a nap")]/../input
    Element Text Should Be    class:todo-count    0 items left