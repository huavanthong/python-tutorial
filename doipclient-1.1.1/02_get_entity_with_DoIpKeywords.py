from doipclient import DoIPClient

class DoipKeywords(object):

    def get_entity(
        self,
        ecu_ip_address="255.255.255.255", 
        protocol_version=0x02, 
        eid=None, 
        vin=None,
    ):
        if ecu_ip_address is None:
            ecu_ip_address = "255.255.255.255"
        
        
        try:
            address, announcement = DoIPClient.get_entity(ecu_ip_address, protocol_version=0x02, eid=None, vin=None)
            logical_address = announcement.logical_address
            ip, port = address
            print(f"ECU IP Address: {ip}")
            print(f"ECU Logical Address: {logical_address}")
            print(f"Port: {port}")
        except Exception as e:
            print(f"An error occurred while sending a VehicleIdentificationRequest: {e}")

# Tạo một đối tượng của lớp DoipKeywords
test =  DoipKeywords()
# Gọi phương thức get_entity từ đối tượng đã tạo
test.get_entity()
