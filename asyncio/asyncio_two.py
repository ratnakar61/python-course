import asyncio
import time

async def brew_chai(name):
    print(f"{name} chai is brewing...")
    #await asyncio.sleep(3)
    time.sleep(3)
    print(f"{name} chai is ready...")

async def main():
    await asyncio.gather (
        brew_chai("Masala"),
        brew_chai("Green"),
        brew_chai("Ginger"),
    )

asyncio.run(main())