""""
Có thể sử dụng thư viện socket cho cả UDP và TCP trên cùng một máy tính, và trong nhiều trường hợp, điều này là cần thiết. 
Socket là một giao diện chung để làm việc với mạng và cho phép bạn tạo và quản lý các kết nối UDP và TCP riêng biệt.

Dưới đây là một ví dụ về cách sử dụng socket cho cả UDP và TCP trong Python:
"""
import socket

# Tạo một socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tạo một socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Kết nối TCP
tcp_socket.connect(("example.com", 80))

# Gửi dữ liệu qua TCP
tcp_socket.send(b"Hello, TCP!")

# Nhận dữ liệu từ UDP
udp_socket.bind(("0.0.0.0", 12345))
data, addr = udp_socket.recvfrom(1024)

# Đóng các socket khi hoàn thành
tcp_socket.close()
udp_socket.close()
