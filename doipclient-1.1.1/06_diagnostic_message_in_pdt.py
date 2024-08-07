import binascii
from doipclient import DoIPClient

client = DoIPClient(ecu_ip_address='10.200.220.1',ecu_logical_address=0x747, 
                    client_ip_address='10.200.220.10',client_logical_address=0x767,
                    activation_type=0)

user_data_hex = '1001'
msg = bytes.fromhex(user_data_hex)

client.send_diagnostic(msg)

resp = client.receive_diagnostic()

print(resp)

hex_string = binascii.hexlify(resp).decode('utf-8')
print(hex_string)
