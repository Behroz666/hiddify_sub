import asyncio
from telegram import fetch_recent_posts

if __name__ == "__main__":
    channel = "oneclickvpnkeys"

    recent_posts = asyncio.run(fetch_recent_posts(channel, days=1))

    for i, post in enumerate(recent_posts, 1):
        print(f"Post {i}:")
        print(post)
        print("-" * 50)
