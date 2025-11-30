import asyncio
import websockets

async def connect_and_send():
    uri = "ws://localhost:8765"
    print(f"Conectando em {uri}")

    async with websockets.connect(uri) as websocket:
        await websocket.send("Olá servidor!")
        resposta = await websocket.recv()
        print("Resposta:", resposta)

asyncio.run(connect_and_send())
