import asyncio
import websockets

from src.settings import SERVER_HOST, SERVER_PORT

connected_clients = set()


async def handle_client(websocket, path):
    connected_clients.add(websocket)

    try:
        async for message in websocket:
            await broadcast_message(message)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)


async def broadcast_message(message):
    for client in connected_clients:
        await client.send(message)


start_server = websockets.serve(handle_client, SERVER_HOST, SERVER_PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
