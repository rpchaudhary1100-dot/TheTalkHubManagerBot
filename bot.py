import os
import asyncio
from pyrogram import Client, filters

API_ID = int(os.environ.get("API_ID", "123456"))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

bot = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(f"Hello {message.from_user.mention}! Main live hoon. 🚀")

async def main():
    print("Bot start ho raha hai...")
    await bot.start()
    print("Bot successfully live ho gaya!")
    # Keep running
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())


