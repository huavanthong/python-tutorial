from doipclient import DoIPClient

client = DoIPClient(ecu_ip_address='192.168.108.1',ecu_logical_address=4444)

print(client.request_alive_check())
print("[RoutingRequest] Start")
print(client.request_activation(activation_type=2))