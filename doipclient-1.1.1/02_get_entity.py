from doipclient import DoIPClient

address, announcement = DoIPClient.get_entity()
logical_address = announcement.logical_address
ip, port = address
print(ip, port, logical_address)