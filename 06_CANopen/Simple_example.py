import canopen

# Tạo một đối tượng CANopen
network = canopen.Network()

# Kết nối đến thiết bị CANopen
network.connect(bustype='socketcan', channel='can0')

# Lấy đối tượng CANopen cho một node cụ thể
node = network.add_node(1, 'node_definition.eds')

# Đọc hoặc ghi dữ liệu từ hoặc vào node
node.sdo['object_index'].raw = 123  # Ví dụ ghi dữ liệu

# Đóng kết nối CANopen
network.disconnect()
