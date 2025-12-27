from multiprocessing import Process
import time

def crunch_counter():
    print("Started Counting...")

    count = 0
    for _ in range(100_000_000):
        count += 1

    print("Ended Counting...")

if __name__ == "__main__":
    start = time.time()

    p1 = Process(target=crunch_counter)
    p2 = Process(target=crunch_counter)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()

    print(f"Total time taken {end - start:.2f} Seconds")