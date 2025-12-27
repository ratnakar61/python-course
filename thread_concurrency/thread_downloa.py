import threading
import requests
import time

def download(url):
    print(f"Starting Download from {url}")
    response  = requests.get(url)
    print(f"Downloaded Image from {url} & size of it {len(response.content)} bytes")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg"
]

start = time.time()

threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url, ))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

end = time.time()

print(f"Total time taken: {end - start:.2f} Seconds")