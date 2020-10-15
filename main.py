import asyncio, json, os
from magix_client import MagixHttpClient

magix_host = os.getenv('MAGIX_HOST', 'http://localhost:8080')


async def main():
    client = MagixHttpClient(magix_host)

    client.observe().subscribe(lambda event: print(json.loads(event.data)))
    client.observe().subscribe(lambda event: print(json.loads(event.data)))
    client.observe().subscribe(lambda event: print(json.loads(event.data)))
    client.broadcast({'hello': 'world'})
    await asyncio.sleep(30)


if __name__ == "__main__":
    asyncio.run(main())
