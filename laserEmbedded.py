import random
import asyncio
from actorio import Actor, Message, DataMessage, ask, EndMainLoop, Reference

class Laser(Actor):
    async def handle_message(self, message: Message):
        print("Laser")
        # await asyncio.sleep(1)
        print("Unitialised")
        # await asyncio.sleep(1)
        print("Initialising")
        # await asyncio.sleep(1)
        print("Initialised")
        # await asyncio.sleep(1)
        print("Configuring")
        # await asyncio.sleep(1)
        print("Configured")
        # await asyncio.sleep(1)
        await message.sender.tell(DataMessage(data="Hello World Im a laser!" +"\n", sender=self))
async def main():
    # Let's create an instance of a Greeter actor and start it. 
    async with Laser() as laser:
        # Then we'll just send it an empty message and wait for a response
        reply : DataMessage = await ask(laser, Message())
    print(reply.data)
asyncio.get_event_loop().run_until_complete(main())