import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.exceptions import TelegramBadRequest

from keyboards.menu import join_keyboard

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 Welcome to TradeLearn Hub!\n\n"
        "To continue using this bot, please join our official channel first.",
        reply_markup=join_keyboard
    )


@dp.callback_query(lambda c: c.data == "verify")
async def verify(callback: CallbackQuery):
    try:
        member = await bot.get_chat_member(
            chat_id="@tradelearnhub12",
            user_id=callback.from_user.id
        )

        if member.status in ["member", "administrator", "creator"]:
            await callback.message.edit_text(
                "🎉 Verification Successful!\n\n"
                "✅ You have joined TradeLearn Hub.\n\n"
                "More features are coming soon!"
            )
        else:
            await callback.answer(
                "❌ Please join the channel first.",
                show_alert=True
            )

    except TelegramBadRequest:
        await callback.answer(
            "⚠️ Verification failed. Please try again.",
            show_alert=True
        )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
