from selenium import webdriver

# Khởi tạo trình điều khiển của Firefox
driver = webdriver.Firefox()

# Mở trang web
driver.get("https://www.example.com")

# Lấy tiêu đề của trang
print(driver.title)

# Đóng trình duyệt
driver.quit()
