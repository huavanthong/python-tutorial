from doipclient import DoIPClient

client = DoIPClient(ecu_ip_address='10.200.220.1',ecu_logical_address=1863, 
                    client_ip_address='10.200.220.10',client_logical_address=1895,
                    activation_type=0)

print(client.send_diagnostic(b'3E80', timeout=200))
