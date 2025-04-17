""""
Tuyệt vời, bạn muốn xây dựng một main process điều khiển 2 process con, và có khả năng gửi tín hiệu (signal) tới các process con
giống như kiểu quản lý tiến trình kiểu "master-worker" hoặc "controller-subprocess".

Dưới đây là ví dụ chi tiết về:
+ Tạo 2 process con
+ Main process quản lý, gửi tín hiệu (ví dụ: SIGTERM) tới từng process con
+ Process con xử lý tín hiệu (bắt SIGTERM và thoát một cách an toàn)

Output demo:
🧠 Main controller starting 2 workers...
📦 Process 1 PID: 12345
📦 Process 2 PID: 12346
[Main] Running controller loop 0
[Process 1] Working...
[Process 2] Doing something...
...
[Main] Sending SIGTERM to both workers...
[Process 1] Received SIGTERM. Exiting...
[Process 2] Received SIGTERM. Exiting...
✅ All workers exited cleanly.

"""

import multiprocessing
import time
import os
import signal
import sys

# Process 1
def worker_one():
    def handle_sigterm(signum, frame):
        print("[Process 1] Received SIGTERM. Exiting...")
        sys.exit(0)

    signal.signal(signal.SIGTERM, handle_sigterm)

    while True:
        print("[Process 1] Working...")
        time.sleep(1)

# Process 2
def worker_two():
    def handle_sigterm(signum, frame):
        print("[Process 2] Received SIGTERM. Exiting...")
        sys.exit(0)

    signal.signal(signal.SIGTERM, handle_sigterm)

    while True:
        print("[Process 2] Doing something...")
        time.sleep(1)

if __name__ == "__main__":
    print("🧠 Main controller starting 2 workers...")

    p1 = multiprocessing.Process(target=worker_one)
    p2 = multiprocessing.Process(target=worker_two)

    p1.start()
    p2.start()

    print(f"📦 Process 1 PID: {p1.pid}")
    print(f"📦 Process 2 PID: {p2.pid}")

    try:
        # Main loop (controller logic)
        for i in range(10):
            print(f"[Main] Running controller loop {i}")
            time.sleep(1)

        print("[Main] Sending SIGTERM to both workers...")
        os.kill(p1.pid, signal.SIGTERM)
        os.kill(p2.pid, signal.SIGTERM)

        p1.join()
        p2.join()
        print("✅ All workers exited cleanly.")

    except KeyboardInterrupt:
        print("\n[Main] Caught CTRL+C. Terminating workers...")
        p1.terminate()
        p2.terminate()
