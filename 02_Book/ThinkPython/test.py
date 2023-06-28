

def process_string(string):
    # Tạo chuỗi lặp lại
    repeated_string = string * 3

    # Cắt chuỗi thành các phần nhỏ hơn
    cut_string_1 = string[:len(string)//2]
    cut_string_2 = string[len(string)//2:]

    return repeated_string, cut_string_1, cut_string_2

# Thử nghiệm
text = "Hello World"
repeated, cut1, cut2 = process_string(text)

print("Chuỗi lặp lại:", repeated)
print("Phần cắt 1:", cut1)
print("Phần cắt 2:", cut2)
