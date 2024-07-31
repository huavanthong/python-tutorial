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

*** Keywords ***
Click Play Button If Needed
    [Documentation]    Kiểm tra và nhấp vào nút Play nếu cần thiết
    ${play_button_present}=    Run Keyword And Return Status    Element Should Be Visible    css:button.ytp-large-play-button.ytp-button
    Run Keyword If    ${play_button_present}    Click Element    css:button.ytp-large-play-button.ytp-button
