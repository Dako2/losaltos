import asyncio
import websockets
import json

async def echo(websocket, path):
    async for message in websocket:
        # Assuming the message is in JSON format
        angles = json.loads(message)
        #print(f"Received angles: {angles}")
        print(int(float(angles['y'])/3.1415926*4096))

start_server = websockets.serve(echo, "0.0.0.0", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

