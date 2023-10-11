import socket

# Địa chỉ và cổng của máy chủ DoIP
server_ip = "127.0.0.1"  # Thay thế bằng địa chỉ IP của máy chủ
tcp_port = 13400  # Cổng TCP của máy chủ DoIP
udp_port = 13401  # Cổng UDP của máy chủ DoIP

# Dữ liệu bạn muốn gửi
tcp_data = "Hello via TCP from DoIP client!"
udp_data = "Hello via UDP from DoIP client!"

# Gửi dữ liệu qua TCP
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client_socket.connect((server_ip, tcp_port))
tcp_client_socket.send(tcp_data.encode('utf-8'))
tcp_response = tcp_client_socket.recv(1024)
print(f"Received TCP response: {tcp_response.decode('utf-8')}")
tcp_client_socket.close()

# Gửi dữ liệu qua UDP
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_client_socket.sendto(udp_data.encode('utf-8'), (server_ip, udp_port))
udp_response, udp_server_address = udp_client_socket.recvfrom(1024)
print(f"Received UDP response from {udp_server_address}: {udp_response.decode('utf-8')}")
udp_client_socket.close()
