import functools
import asyncio

def executor(func):
    @functools.wraps(func)
    async def inner(*args, **kwargs):
        loop = asyncio.get_event_loop()
        thing = functools.partial(func, *args, **kwargs)
        return await loop.run_in_executor(None, thing)
    return inner