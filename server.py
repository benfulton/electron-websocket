#!/usr/bin/env python

import asyncio
import websockets
import sys

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', int(sys.argv[1])))

asyncio.get_event_loop().run_forever()
print("Complete")
