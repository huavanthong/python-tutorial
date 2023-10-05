import socket

# Địa chỉ IP và cổng của máy chủ UDP
server_ip = "127.0.0.1"  # Thay thế bằng địa chỉ IP của máy chủ thực tế
server_port = 12345  # Thay thế bằng cổng của máy chủ thực tế

# Tạo một socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Dữ liệu bạn muốn gửi
data_to_send = "Hello, server!"

# Gửi dữ liệu đến máy chủ
client_socket.sendto(data_to_send.encode('utf-8'), (server_ip, server_port))

# Nhận phản hồi từ máy chủ
response, server_address = client_socket.recvfrom(1024)

# In phản hồi từ máy chủ
print(f"Received response: {response.decode('utf-8')} from {server_address}")

# Đóng socket khi hoàn thành
client_socket.close()
