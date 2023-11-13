import socket

# Thiết lập địa chỉ và cổng cho máy chủ DoIP
ip_address = "127.0.0.1"  # Thay thế bằng địa chỉ IP của máy chủ
tcp_port = 13400  # Cổng TCP cho DoIP
udp_port = 13401  # Cổng UDP cho DoIP

# Thiết lập socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((ip_address, tcp_port))
tcp_socket.listen(1)

# Thiết lập socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((ip_address, udp_port))

print(f"Server is listening on {ip_address}:{tcp_port} (TCP) and {ip_address}:{udp_port} (UDP)")

while True:
    # Xử lý kết nối TCP
    tcp_client_socket, tcp_client_address = tcp_socket.accept()
    print(f"Accepted TCP connection from {tcp_client_address}")
    tcp_data = tcp_client_socket.recv(1024)
    print(f"Received TCP data: {tcp_data.decode('utf-8')}")
    tcp_client_socket.close()

    # Xử lý gửi/nhận dữ liệu UDP
    udp_data, udp_client_address = udp_socket.recvfrom(1024)
    print(f"Received UDP data from {udp_client_address}: {udp_data.decode('utf-8')}")
    udp_socket.sendto(b"Hello from DoIP server!", udp_client_address)
