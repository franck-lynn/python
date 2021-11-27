import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    
    
async def main():
    # 创建任务
    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))
    
    print("started")
    await task1
    await task2
    
asyncio.run(main())    
    