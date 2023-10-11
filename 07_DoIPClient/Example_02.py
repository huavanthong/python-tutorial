"""
Trong ví dụ này, chúng ta sử dụng socket để tạo một socket UDP và gửi một DoIP Alive Check Request đến máy chủ DoIP theo địa chỉ IP 
và cổng được xác định. Sau đó, chúng ta đợi phản hồi từ máy chủ (có thể đặt thời gian chờ tối đa). Phản hồi được nhận và hiển thị.
"""
import socket

# Địa chỉ IP và cổng của máy chủ DoIP
server_ip = '192.168.1.100'  # Thay đổi thành địa chỉ IP của máy chủ DoIP
server_port = 13400          # Thay đổi thành cổng DoIP của máy chủ

# Tạo socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Dữ liệu của DoIP Alive Check Request (ví dụ: các trường dữ liệu)
request_data = b'\x02\x00\x00\x00\x00\x00\x00\x00'

# Gửi yêu cầu đến máy chủ DoIP
client_socket.sendto(request_data, (server_ip, server_port))

# Đợi nhận phản hồi từ máy chủ DoIP (có thể đặt timeout)
client_socket.settimeout(5)  # Đợi tối đa 5 giây
try:
    response_data, server_address = client_socket.recvfrom(1024)
    print(f"Đã nhận phản hồi từ {server_address}: {response_data}")
except socket.timeout:
    print("Không nhận được phản hồi sau 5 giây.")

# Đóng socket
client_socket.close()
