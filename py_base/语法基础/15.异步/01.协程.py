# https://docs.python.org/zh-cn/3/library/asyncio-task.html
import asyncio
import time

# async def main():
#     print("hello")
#     await asyncio.sleep(1)
#     print("world")

# asyncio.run(main())

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())

asyncio.run(main())