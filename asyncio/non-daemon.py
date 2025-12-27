import threading
import time

def monitor_tea_temperature():
    while True:
        print(f"Monitoring tea temperature...")
        time.sleep(2)

t = threading.Thread(target=monitor_tea_temperature)

t.start()

print("program done")