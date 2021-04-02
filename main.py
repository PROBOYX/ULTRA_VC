from pyrogram import Client as Bot
import os
os.system("pip install telethon")
from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN
from telethon import TelegramClient, Button

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

xbot = TelegramClient("PROBOYX", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

bot.start()
run()
@xbot.on(events.NewMessage(pattern="/owner"))
async def owner (event):
  await xbot.send_message(event.chat_id, "THIS IS MY OWNER", buttons=[[Button.url("PROBOYX", "https://t.me/proboyx")]])

if __name__ == '__main__':
  xbot.run_until_disconnected()
