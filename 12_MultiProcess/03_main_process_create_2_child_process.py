""""
Mục tiêu:
+ Có 1 main process
+ Main process sẽ tạo ra 2 child process
+ Mỗi child process thực hiện một công việc đơn giản (in log, sleep...)
"""
import multiprocessing
import time
import os

# Child Process 1
def child_one():
    print(f"[Child 1] PID: {os.getpid()} | Parent PID: {os.getppid()}")
    for i in range(5):
        print(f"[Child 1] Working {i}")
        time.sleep(1)

# Child Process 2
def child_two():
    print(f"[Child 2] PID: {os.getpid()} | Parent PID: {os.getppid()}")
    for i in range(5):
        print(f"[Child 2] Doing task {i}")
        time.sleep(1)

if __name__ == "__main__":
    print(f"🧠 Main process PID: {os.getpid()}")

    # Tạo 2 child process
    p1 = multiprocessing.Process(target=child_one)
    p2 = multiprocessing.Process(target=child_two)

    # Khởi động child process
    p1.start()
    p2.start()

    # Đợi cả 2 process hoàn thành
    p1.join()
    p2.join()

    print("✅ Main process: All child processes completed.")
