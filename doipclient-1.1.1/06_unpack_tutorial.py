# Giá trị số nguyên
user_data_value = 1001

# Số byte bạn muốn sử dụng để biểu diễn giá trị (2 byte trong trường hợp này)
num_bytes = 2

# Định dạng mạng (big-endian)
byte_order = 'big'

# Chuyển giá trị số nguyên thành bytes
user_data_bytes = user_data_value.to_bytes(num_bytes, byte_order)

# Hiển thị kết quả
print(user_data_bytes)