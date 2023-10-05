*** Settings ***
Library           TCP/IP

*** Test Cases ***
Test DoIP Communication
    # Thiết lập kết nối TCP/IP đến thiết bị DoIP (ví dụ: 192.168.1.100:13400)
    Open Connection    192.168.1.100    13400

    # Gửi yêu cầu "Vehicle Identification Request"
    ${request}=    Set Variable    02 00 00 00
    Send Bytes    ${request}

    # Nhận phản hồi từ thiết bị DoIP
    ${response}=    Receive Bytes

    # Đóng kết nối TCP/IP
    Close Connection

    # Kiểm tra xem phản hồi có đúng định dạng "Vehicle Identification Response" không
    Should Be Equal As Bytes    ${response}    02 00 00 08 00 00 00 04 00 00 00

    # Kiểm tra nội dung của phản hồi (ví dụ: xác định mã sản phẩm)
    ${product_code}=    Get Bytes    ${response}[8:12]
    Should Be Equal As Bytes    ${product_code}    00 00 00 04
