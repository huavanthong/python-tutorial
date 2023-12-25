from doipclient import DoIPClient
from doipclient.messages import *
 
address, announcement = DoIPClient.get_entity()
logical_address = announcement.logical_address
ip, port = address
print(ip, port, logical_address)

client = DoIPClient(ip, logical_address)
print(client.send_diagnostic(b'3E80', timeout=200))
