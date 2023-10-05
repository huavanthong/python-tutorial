# If you want to check server is active
# ping www.google.com
import socket 

ip = socket.gethostbyname('www.google.com')
print(ip)