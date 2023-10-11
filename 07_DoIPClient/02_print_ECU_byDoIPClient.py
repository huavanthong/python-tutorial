from doipclient import DoIPClient
address, announcement = DoIPClient.await_vehicle_announcement()
# Power cycle your ECU and wait for a few seconds for the broadcast to be
# received
logical_address = announcement.logical_address
ip, port = address
print(ip, port, logical_address)