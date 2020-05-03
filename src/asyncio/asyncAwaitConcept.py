import asyncio
import time


async def hello():
    print("before await")

    r = await num()
    print("after await", r)


async def num():
    print("number block")
    return "hello"

loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
