'''
Trong Python khi tạo socket, nếu bạn không chỉ định giao thức cụ thể cho socket, thì mặc định sẽ sử dụng giao thức TCP (IPPROTO_TCP). 
Trong trường hợp của việc sử dụng socket.SOCK_DGRAM (UDP) như trong đoạn mã trên, đó là đủ để chỉ định giao thức là UDP, 
và bạn không cần phải sử dụng IPPROTO_UDP.
Nhưng nếu bạn muốn rõ ràng hơn và chắc chắn, bạn có thể sử dụng IPPROTO_UDP như sau:
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
'''
import socket

class MyUDPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = None

    def start(self):
        try:
            # Tạo socket với IPv4 và giao thức UDP
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            # Option: SO_REUSEADDR để có thể sử dụng địa chỉ đã bị chiếm
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # Gắn kết địa chỉ và cổng
            self.sock.bind((self.host, self.port))

            print(f"Server is listening on {self.host}:{self.port}")

            # Lắng nghe gói tin
            while True:
                data, addr = self.sock.recvfrom(1024)
                print(f"Received data from {addr}: {data.decode('utf-8')}")

        except Exception as e:
            print(f"Error: {e}")

    def stop(self):
        if self.sock:
            self.sock.close()

if __name__ == "__main__":
    server = MyUDPServer('0.0.0.0', 12345)
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()
        print("Server stopped.")
