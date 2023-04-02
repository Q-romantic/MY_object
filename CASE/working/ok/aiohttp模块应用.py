import asyncio
import aiohttp

urls = [
    "http://kr.shanghai-jiuxin.com/file/2022/0407/00ecf86cbb9d448ac36536c8f370218d.jpg",
    "http://kr.shanghai-jiuxin.com/file/2022/0414/dcc60948244f0d7f6adc7c3ff4da87eb.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/a2c58d6d726fb7ef29390becac5d8643.jpg"
]



async def aiodownload(url):
    name = url.rsplit("/", 1)[1]  # 从右边切，切一次。得到[1]位置的内容
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open(name, mode="wb") as f:
                f.write(await resp.content.read())  # 读取内容是异步的。需要await挂起
                # f.write(await resp.text())  # 文本写入
    print(name, "ok")


async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(aiodownload(url)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    # asyncio.run(main())
    asyncio.get_event_loop().run_until_complete(main())  # 新版本代替以上方法
