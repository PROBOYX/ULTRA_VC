from pyrogram import Client as Bot
import os
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

bot.start()
run()
