from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅Tasdiqlash", callback_data="tasdiq"),
            InlineKeyboardButton(text="❌Rad etish", callback_data="rad"),
        ]
    ])
