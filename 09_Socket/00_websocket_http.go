```
Trong mã này:

1. Chúng tôi sử dụng thư viện Gorilla WebSocket để hỗ trợ WebSocket.
2. Chúng tôi tạo hai xử lý HTTP khác nhau: httpHandler cho endpoints HTTP thông thường và websocketHandler cho endpoints WebSocket.
3. Endpoint HTTP chỉ trả về một thông báo văn bản đơn giản.
4. Endpoint WebSocket thiết lập một kết nối WebSocket và trao đổi dữ liệu với khách hàng.

Khi bạn chạy chương trình này, bạn có thể truy cập máy chủ HTTP tại http://localhost:8080/ và máy chủ WebSocket tại ws://localhost:8080/websocket.
Sự khác nhau cơ bản là rằng máy chủ WebSocket cho phép trao đổi dữ liệu hai chiều liên tục, trong khi máy chủ HTTP chỉ trả về dữ liệu khi bạn gửi yêu cầu HTTP.
```
package main

import (
	"fmt"
	"net/http"

	"github.com/gorilla/websocket"
)

var upgrader = websocket.Upgrader{
	ReadBufferSize:  1024,
	WriteBufferSize: 1024,
}

func httpHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "This is an HTTP endpoint")
}

func websocketHandler(w http.ResponseWriter, r *http.Request) {
	conn, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer conn.Close()

	fmt.Println("WebSocket connection established")

	for {
		messageType, p, err := conn.ReadMessage()
		if err != nil {
			fmt.Println(err)
			return
		}
		fmt.Printf("Received message: %s\n", p)

		err = conn.WriteMessage(messageType, p)
		if err != nil {
			fmt.Println(err)
			return
		}
		fmt.Println("Sent message back to client")
	}
}

func main() {
	http.HandleFunc("/", httpHandler)
	http.HandleFunc("/websocket", websocketHandler)

	http.ListenAndServe(":8080", nil)
}
