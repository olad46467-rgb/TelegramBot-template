import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")

ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

BOT_NAME = os.getenv("BOT_NAME", "Telegram Bot")

WELCOME_MESSAGE = os.getenv(
    "WELCOME_MESSAGE",
    "👋 Welcome! Please join our official channel before continuing."
)
