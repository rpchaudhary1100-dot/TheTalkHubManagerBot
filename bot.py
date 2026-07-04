())
import os
import asyncio
from pyrogram import Client, filters

# Environment variables se credentials uthana
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
    await message.reply_text(f"Hello {message.from_user.mention}! Main live hoon aur perfectly kaam kar raha hoon. 🚀")

async def main():
    print("Bot chalu ho raha hai...")
    await bot.start()
    print("Bot live hai!")
    from pyrogram.methods.utilities.idle import idle
    await idle()
    await bot.stop()

if __name__ == "__main__":
    # Python 3.14+ ke liye naya loop handler setup
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    loop.run_until_complete(main())
