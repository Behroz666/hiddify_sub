from telethon import TelegramClient
from datetime import datetime, timedelta
import asyncio
import os

api_id = int(os.environ["TG_API_ID"])
api_hash = os.environ["TG_API_HASH"]

async def fetch_recent_posts(channel_username: str, days: int = 1) -> list:
    
    client = TelegramClient("session", api_id, api_hash)

    await client.start()

    entity = await client.get_entity(channel_username)
    time_threshold = datetime.utcnow() - timedelta(days=days)

    posts = []

    async for message in client.iter_messages(entity, limit=100):
        if message.date >= time_threshold:
            if message.text:
                posts.append(message.text)
        else:
            break

    await client.disconnect()
    return posts
