from typing import Optional

def connect_to_ecu(ecu_ip_address, client_logical_address=0x0E00):
    if ecu_ip_address is not None:
        print(f"Connecting to the ecu ip address: {ecu_ip_address}; client: {client_logical_address}")
    else:
        print("Ecu address not found")

def connect_to_database(dbName: Optional[str] = None):
    if dbName is not None:
        print(f"Connecting to the database: {dbName}")
    else:
        print("No database name provided")



connect_to_ecu("192.168.1.10")


connect_to_ecu()



# Sử dụng với tên cơ sở dữ liệu
connect_to_database("my_database")

# Sử dụng mà không cung cấp tên cơ sở dữ liệu
connect_to_database()

# Sử dụng với giá trị None
connect_to_database(None)



