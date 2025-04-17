import multiprocessing
import time

# Hàm cho process 1
def process_one():
    for i in range(5):
        print(f"[Process 1] Tick {i}")
        time.sleep(1)

# Hàm cho process 2
def process_two():
    for i in range(5):
        print(f"[Process 2] Tock {i}")
        time.sleep(1)

if __name__ == "__main__":
    # Tạo 2 process
    p1 = multiprocessing.Process(target=process_one)
    p2 = multiprocessing.Process(target=process_two)

    # Bắt đầu 2 process
    p1.start()
    p2.start()

    # Đợi cả hai process hoàn thành
    p1.join()
    p2.join()

    print("🏁 Main program done.")
