"""
Trong ví dụ này, chúng ta tạo một socket UDP và một socket TCP, sau đó lắng nghe trên các cổng UDP và TCP khác nhau.
Máy chủ có khả năng xử lý dữ liệu từ cả hai giao thức UDP và TCP và phản hồi lại cho các yêu cầu từ client.
"""
import socket

# Địa chỉ và cổng cho máy chủ UDP và TCP
udp_host = "0.0.0.0"  # Lắng nghe trên tất cả các địa chỉ IP
udp_port = 12345  # Chọn một cổng UDP tự chọn (trong khoảng 1-65535)

tcp_host = "0.0.0.0"  # Lắng nghe trên tất cả các địa chỉ IP
tcp_port = 54321  # Chọn một cổng TCP tự chọn (trong khoảng 1-65535)

# Tạo socket UDP và kết nối
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((udp_host, udp_port))

# Tạo socket TCP và kết nối
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((tcp_host, tcp_port))
tcp_socket.listen(5)  # Số lượng kết nối tối đa đợi trong hàng đợi

print(f"Server is listening on UDP port {udp_port} and TCP port {tcp_port}")

while True:
    try:
        # Xử lý kết nối UDP
        udp_data, udp_addr = udp_socket.recvfrom(1024)
        print(f"Received UDP data from {udp_addr}: {udp_data.decode('utf-8')}")

        # Xử lý kết nối TCP
        tcp_client_socket, tcp_client_address = tcp_socket.accept()
        tcp_data = tcp_client_socket.recv(1024)
        print(f"Received TCP data from {tcp_client_address}: {tcp_data.decode('utf-8')}")
        tcp_client_socket.send(b"Hello, TCP client!")

    except KeyboardInterrupt:
        break

# Đóng cả hai socket khi hoàn thành
udp_socket.close()
tcp_socket.close()
