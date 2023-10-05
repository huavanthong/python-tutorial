import socket

# Tạo một socket CAN
sock = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)

# Gắn kết socket với một giao diện CAN cụ thể (ví dụ: can0)
interface = "can0"
sock.bind((interface,))

while True:
    try:
        # Nhận dữ liệu CAN từ giao diện
        can_frame, addr = sock.recvfrom(16)
        print("Received CAN frame:", can_frame)
        
        # Xử lý dữ liệu CAN ở đây
        # ...
    except KeyboardInterrupt:
        break

# Đóng socket khi hoàn thành
sock.close()
