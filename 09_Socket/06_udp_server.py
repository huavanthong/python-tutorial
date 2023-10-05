import socket

# Địa chỉ IP và cổng để máy chủ lắng nghe
server_ip = "0.0.0.0"  # Lắng nghe trên tất cả các địa chỉ IP
server_port = 12345  # Chọn một cổng tự chọn (trong khoảng 1-65535)

# Tạo một socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Gắn kết socket với địa chỉ và cổng
server_socket.bind((server_ip, server_port))

print(f"Server is listening on {server_ip}:{server_port}")

while True:
    # Nhận dữ liệu từ khách hàng
    data, client_address = server_socket.recvfrom(1024)
    
    # In dữ liệu và địa chỉ của khách hàng
    print(f"Received data: {data.decode('utf-8')} from {client_address}")
    
    # Phản hồi lại khách hàng (có thể xử lý dữ liệu ở đây)
    response = "Hello, client!"
    server_socket.sendto(response.encode('utf-8'), client_address)
