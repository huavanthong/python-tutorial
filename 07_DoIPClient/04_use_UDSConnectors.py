from doipclient import DoIPClient
from your_module import DoIPClientUDSConnector

# Khởi tạo đối tượng DoIPClient
doip_client = DoIPClient()

# Khởi tạo kết nối UDS
uds_connector = DoIPClientUDSConnector(doip_client, name="MyUDSConnection")

# Mở kết nối
uds_connector.open()

# Sử dụng kết nối để gửi và nhận dữ liệu UDS
uds_connector.specific_send(b"\x10\x02")
response = uds_connector.specific_wait_frame()

# Đóng kết nối (tuỳ chọn)
uds_connector.close()
