import socket

# Địa chỉ multicast và cổng mặc định cho truy vấn mạng DoIP
DOIP_MULTICAST_ADDRESS = "ff02::1"
DOIP_PORT = 13400

# Tạo socket UDP
udp_socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

# Gửi truy vấn mạng
query_message = b"\x02\x00\x00\x00\x00\x01\x02\x00"
udp_socket.sendto(query_message, (DOIP_MULTICAST_ADDRESS, DOIP_PORT))

# Nhận phản hồi
response, address = udp_socket.recvfrom(1024)

# Xử lý phản hồi để lấy địa chỉ logic
if len(response) >= 8:
    logical_address = response[4:8]
    print("Logical Address:", logical_address.hex())
else:
    print("Không thể lấy địa chỉ logic.")

# Đóng socket
udp_socket.close()
