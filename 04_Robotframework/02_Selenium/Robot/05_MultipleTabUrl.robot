*** Settings ***
Documentation     Mở video trên YouTube trong nhiều tab cùng lúc, tắt tiếng và tự động phát
Library           SeleniumLibrary

*** Variables ***
${YOUTUBE_URL}    https://www.youtube.com/watch?v=cXNwAk-ECCo    # Replace VIDEO_ID with the actual YouTube video ID
${BROWSER}        Firefox
${NUM_TABS}       3    # Number of tabs to open

*** Test Cases ***
Open And Mute YouTube Videos In Multiple Tabs
    [Documentation]    Mở video trên YouTube trong nhiều tab, tắt tiếng và tự động phát
    Open Browser To YouTube In First Tab
    FOR    ${i}    IN RANGE    ${NUM_TABS} - 1
        Open New Tab And Mute Video
    END
    Wait For Videos To Play Help Us Increase Views
    Close Browser

*** Keywords ***
Open Browser To YouTube In First Tab
    Open Browser    ${YOUTUBE_URL}    ${BROWSER}
    Maximize Browser Window
    Mute And Play Video

Open New Tab And Mute Video
    Execute JavaScript    window.open("${YOUTUBE_URL}", "_blank")
    ${handles}=    Get Window Handles
    Switch Window       ${handles[2]}
    Mute And Play Video

Mute And Play Video
    Wait Until Element Is Visible    id=movie_player
    ${is_paused}=    Run Keyword And Ignore Error    Get Element Attribute    id=movie_player    class
    Run Keyword If    'paused-mode' in ${is_paused}    Click Element    css=button.ytp-play-button
    Click Element    css=button.ytp-mute-button

Wait For Videos To Play Help Us Increase Views
    Sleep    300s
