import random
import asyncio
from actorio import Actor, Message, DataMessage, ask, EndMainLoop, Reference

class Motorized_galvo_wheel(Actor):
    async def handle_message(self, message: Message):
        print("Motorized galvo wheel")
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
        await message.sender.tell(DataMessage(data="Hello World Im a motorized galvo wheel!" + "\n", sender=self))
async def main():
    # Let's create an instance of a Greeter actor and start it. 
    async with Motorized_galvo_wheel() as motorized_galvo_wheel:
        # Then we'll just send it an empty message and wait for a response
        reply : DataMessage = await ask(motorized_galvo_wheel, Message())
    print(reply.data)
asyncio.get_event_loop().run_until_complete(main())