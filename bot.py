import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.exceptions import TelegramBadRequest

from config import (
    BOT_TOKEN,
    WELCOME_MESSAGE,
    CHANNEL_USERNAME,
    BOT_NAME
)

from keyboards.menu import join_keyboard

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# =========================
# START COMMAND
# =========================
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        WELCOME_MESSAGE,
        reply_markup=join_keyboard
    )


# =========================
# VERIFY BUTTON
# =========================
@dp.callback_query(lambda c: c.data == "verify")
async def verify(callback: CallbackQuery):
    try:
        member = await bot.get_chat_member(
            chat_id=CHANNEL_USERNAME,
            user_id=callback.from_user.id
        )

        if member.status in ("member", "administrator", "creator"):
            await callback.message.answer(
                f"🎉 Verification Successful!\n\n"
                f"Welcome to {BOT_NAME}!\n\n"
                "You can now access the bot."
            )
        else:
            await callback.answer(
                "❌ Please join the channel first.",
                show_alert=True
            )

    except TelegramBadRequest:
        await callback.answer(
            "⚠️ Unable to verify membership.",
            show_alert=True
        )


# =========================
# START BOT
# =========================
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
