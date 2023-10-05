"""
Trong ví dụ này:

1. Chúng ta tạo một socket UDP và một socket TCP để gửi dữ liệu đến máy chủ.
2. Dữ liệu bạn muốn gửi là udp_data và tcp_data.
3. Đối với socket UDP, chúng ta sử dụng sendto() để gửi dữ liệu đến máy chủ qua địa chỉ và cổng đã chỉ định.
4. Đối với socket TCP, chúng ta sử dụng connect() để kết nối đến máy chủ và sau đó sử dụng send() để gửi dữ liệu.
5. Chúng ta cũng nhận phản hồi từ máy chủ TCP và in ra nó.

Lưu ý rằng bạn cần thay thế udp_server_address và tcp_server_address bằng địa chỉ và cổng thật của máy chủ UDP và TCP mà bạn đang sử dụng.
"""
import socket

# Địa chỉ và cổng của máy chủ UDP và TCP
udp_server_address = ("127.0.0.1", 12345)  # Thay thế bằng địa chỉ và cổng thật
tcp_server_address = ("127.0.0.1", 54321)  # Thay thế bằng địa chỉ và cổng thật

# Dữ liệu bạn muốn gửi
udp_data = "Hello, UDP server!"
tcp_data = "Hello, TCP server!"

# Tạo socket UDP và gửi dữ liệu
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_client_socket.sendto(udp_data.encode('utf-8'), udp_server_address)
udp_client_socket.close()

# Tạo socket TCP và gửi dữ liệu
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client_socket.connect(tcp_server_address)
tcp_client_socket.send(tcp_data.encode('utf-8'))
tcp_response = tcp_client_socket.recv(1024)
print(f"Received from TCP server: {tcp_response.decode('utf-8')}")
tcp_client_socket.close()
