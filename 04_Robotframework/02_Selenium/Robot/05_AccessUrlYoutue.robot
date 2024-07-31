*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${YOUTUBE_URL}    https://www.youtube.com/watch?v=cXNwAk-ECCo
${BROWSER}        Firefox

*** Test Cases ***
Open and Play YouTube Video
    [Documentation]    Mở video trên YouTube và tự động phát
    Open Browser    ${YOUTUBE_URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    5s  # Đợi trang web tải hoàn tất
    Click Play Button If Needed
    Sleep    300s  # Xem video trong 30 giây
    Close Browser

Open and Mute YouTube Video
    [Documentation]    Mở video trên YouTube, tắt tiếng và tự động phát
    Open Browser    ${YOUTUBE_URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    5s  # Đợi trang web tải hoàn tất
    Click Play Button If Needed
    Mute Video
    Sleep    60s  # Xem video trong 60 giây để đảm bảo lượt xem được tính
    Close Browser

Open and Mute YouTube Video in New Tab
    [Documentation]    Mở video trên YouTube trong tab mới, tắt tiếng và tự động phát, lặp lại hành động này sau khi xong
    Open Browser    ${YOUTUBE_URL}    ${BROWSER}
    Maximize Browser Window
    Click Play Button If Needed
    Mute Video
    # Sleep    300s  # Xem video trong 60 giây để đảm bảo lượt xem được tính
    Open New Tab And Mute Video
    Click Play Button If Needed
    Mute Video
    Sleep    300s  # Xem video trong 60 giây để đảm bảo lượt xem được tính
    Close Browser


*** Keywords ***
Open New Tab
    [Documentation]    Mở một tab mới trong trình duyệt
    Execute Javascript    window.open('about:blank', '_blank');

Click Play Button If Needed
    [Documentation]    Kiểm tra và nhấp vào nút Play nếu cần thiết
    ${play_button_present}=    Run Keyword And Return Status    Element Should Be Visible    css:button.ytp-large-play-button.ytp-button
    Run Keyword If    ${play_button_present}    Click Element    css:button.ytp-large-play-button.ytp-button

Mute Video
    [Documentation]    Kiểm tra và nhấp vào nút Mute nếu cần thiết
    ${mute_button_present}=    Run Keyword And Return Status    Element Should Be Visible    css:button.ytp-mute-button
    Run Keyword If    ${mute_button_present}    Click Element    css:button.ytp-mute-button

Open New Tab And Mute Video
    Execute JavaScript    window.open()
    ${handles}=    Get Window Handles
    Switch Window    ${handles[-1]}
    Go To    ${YOUTUBE_URL}
