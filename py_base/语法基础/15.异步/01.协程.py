# https://docs.python.org/zh-cn/3/library/asyncio-task.html
import asyncio
import time

# async def main():
#     print("hello")
#     await asyncio.sleep(1)
#     print("world")

# asyncio.run(main())

async def count():
    # 先执行 count() 函数的 one, 
    print("One")
    # 这里有阻塞, 再执行第2个 count()
    await asyncio.sleep(1)
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())

asyncio.run(main())