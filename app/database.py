from motor.motor_asyncio import AsyncIOMotorClient
import os

async def get_database():
    client = AsyncIOMotorClient(os.environ["MONGODB_URL"])
    return client.sla_db
