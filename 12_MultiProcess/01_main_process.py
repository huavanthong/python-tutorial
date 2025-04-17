import os
import time

def main():
    print("✅ This is the main process.")
    print(f"🧠 Main Process PID: {os.getpid()}")
    print(f"📌 Parent PID: {os.getppid()}")

    for i in range(5):
        print(f"[Main] Doing work step {i}")
        time.sleep(1)

    print("🏁 Main process finished.")

if __name__ == "__main__":
    main()
