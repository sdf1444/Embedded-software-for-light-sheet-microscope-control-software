import random
import asyncio
from actorio import Actor, Message, DataMessage, ask, EndMainLoop, Reference
from mqtt2 import *

class Laser(Actor):
    async def handle_message(self, message: Message):
        print("Laser")
        # await asyncio.sleep(2)
        print("Unitialised")
        # await asyncio.sleep(2)
        print("Initialising")
        # await asyncio.sleep(2)
        print("Initialised")
        # await asyncio.sleep(2)
        print("Configuring")
        # await asyncio.sleep(2)
        print("Configured")
        # await asyncio.sleep(2)
        await message.sender.tell(DataMessage(data="Hello World Im a laser!" + "\n", sender=self))
async def main():
    # Let's create an instance of a Greeter actor and start it. 
    async with Laser() as laser:
        # Then we'll just send it an empty message and wait for a response
        reply : DataMessage = await ask(laser, Message())
    print(reply.data)
asyncio.get_event_loop().run_until_complete(main())

def subscribe(): 
    client = embedded()
    client.run()

    client.loop_start()
    client.subscribe("microscope/light_sheet_microscope/UI/laser/#")
subscribe()    