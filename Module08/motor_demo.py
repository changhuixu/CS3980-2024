from motor.motor_asyncio import AsyncIOMotorClient
import asyncio


async def main():
    client = AsyncIOMotorClient("mongodb://localhost:27017/my_database")

    default_db = client.get_default_database()
    # print(default_db)
    print(await client.list_database_names())
    # print(await client.server_info())


asyncio.run(main())
