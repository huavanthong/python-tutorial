"""
Trong ví dụ này, chúng ta sẽ sử dụng thư viện socket của Python để tạo một máy chủ DoIP đơn giản để lắng nghe kết nối 
từ các máy khách.
"""

import socket

# Địa chỉ IP và cổng để lắng nghe
HOST = '0.0.0.0'  # Lắng nghe trên tất cả các giao diện mạng
PORT = 13400      # Sử dụng cổng DoIP mặc định

# Tạo socket DoIP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Gán địa chỉ và cổng cho máy chủ
server_socket.bind((HOST, PORT))

# Lắng nghe kết nối đến máy chủ
server_socket.listen(1)
print(f"Đang lắng nghe kết nối trên {HOST}:{PORT}...")

while True:
    # Chấp nhận kết nối từ máy khách
    client_socket, client_address = server_socket.accept()
    print(f"Đã kết nối từ {client_address}")
    
    # Xử lý dữ liệu từ máy khách
    data = client_socket.recv(1024)
    
    # Kiểm tra xem máy khách đã ngắt kết nối hay chưa
    if not data:
        print(f"Kết nối từ {client_address} đã đóng.")
        break
    
    # Xử lý dữ liệu ở đây (ví dụ: giải mã và hiển thị dữ liệu chẩn đoán)
    decoded_data = data.decode('utf-8')
    print(f"Dữ liệu từ {client_address}: {decoded_data}")

    # Phản hồi lại máy khách (nếu cần)
    response_data = "Dữ liệu đã được xử lý thành công."
    client_socket.send(response_data.encode('utf-8'))

# Đóng kết nối
client_socket.close()
server_socket.close()
