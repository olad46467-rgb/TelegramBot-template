import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from config import BOT_TOKEN, WELCOME_MESSAGE
from keyboards.menu import join_keyboard
from handlers.verify import router as verify_router

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Register the Verify handler
dp.include_router(verify_router)


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        WELCOME_MESSAGE,
        reply_markup=join_keyboard
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
