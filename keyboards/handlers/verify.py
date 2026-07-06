from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest

from config import CHANNEL_USERNAME, BOT_NAME

router = Router()


@router.callback_query(lambda c: c.data == "verify")
async def verify(callback: CallbackQuery):

    bot = callback.bot

    try:
        member = await bot.get_chat_member(
            chat_id=CHANNEL_USERNAME,
            user_id=callback.from_user.id
        )

        if member.status in ("member", "administrator", "creator"):

            await callback.message.answer(
                f"🎉 Verification Successful!\n\n"
                f"Welcome to {BOT_NAME}!\n\n"
                "You now have full access."
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
