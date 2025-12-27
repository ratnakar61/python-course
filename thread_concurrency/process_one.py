import threading
import time

def cpu_heavy():
    total = 0

    for i in range(10000000):
        total += i
    
    print(f"Total: {total}")

threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]
start = time.time()
[t.start() for t in threads]
[t.join() for t in threads]
end = time.time()

print(f"Total time taken: {end - start:.2f}")