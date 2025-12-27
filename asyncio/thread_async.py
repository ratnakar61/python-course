import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(name):
    print(f"Checking stock for {name}")
    time.sleep(3)
    return f"stock of {name} : 42"

async def main():
    loops = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = loops.run_in_executor(pool, check_stock, "Masala Chai")
        print(result)

asyncio.run(main())