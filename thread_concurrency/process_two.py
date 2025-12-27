from multiprocessing import Process
import time

def cpu_heavy():
    total = 0

    for i in range(10000000):
        total += i
    
    print(f"Total: {total}")

process = [Process(target=cpu_heavy) for _ in range(2)]
start = time.time()
[t.start() for t in process]
[t.join() for t in process]
end = time.time()

print(f"Total time taken: {end - start:.2f}")