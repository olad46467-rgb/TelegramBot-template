from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

join_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📢 Join TradeLearn Hub",
                url="https://t.me/tradelearnhub12"
            )
        ],
        [
            InlineKeyboardButton(
                text="✅ Verify",
                callback_data="verify"
            )
        ]
    ]
)
