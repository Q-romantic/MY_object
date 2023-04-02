import time
import asyncio

async def func1():
    print('11111')
    # time.sleep(3)
    await asyncio.sleep(3)
    print('11111')

async def func2():
    print('22222')
    # time.sleep(2)
    await asyncio.sleep(2)
    print('22222')

async def func3():
    print('33333')
    # time.sleep(4)
    await asyncio.sleep(4)
    print('33333')


async def main():
    tasks = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]
    await asyncio.wait(tasks)

if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2 -t1)







