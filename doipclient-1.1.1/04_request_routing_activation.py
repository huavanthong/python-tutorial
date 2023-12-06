from doipclient import DoIPClient

address, announcement = DoIPClient.get_entity()
logical_address = announcement.logical_address
ip, port = address
print(ip, port, logical_address)

client = DoIPClient(ip, logical_address)
print(client.request_activation(activation_type=0, vm_specific="0x0e80"))