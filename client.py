import asyncio
import websockets

#echo "123123" | nc 10.10.1.202 5678
async def send_message(message = "678"):
    uri = "ws://10.10.1.202:5678"
    try:
        async with websockets.connect(uri) as websocket:
            print(f"Sending: {message}")
            await websocket.send(message)

            # Wait for and print response (if you want the client to also receive messages)
            response = await websocket.recv()
            print(f"Received: {response}")
    except OSError as e:
        print(f"Failed to send {message} connect or send a message: {e}")

asyncio.get_event_loop().run_until_complete(send_message())
