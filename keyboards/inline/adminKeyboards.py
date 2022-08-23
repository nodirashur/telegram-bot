from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


menuAdmin = InlineKeyboardMarkup(row_width=5)

set1 = InlineKeyboardButton('1', callback_data='btn1')
set2 = InlineKeyboardButton('2', callback_data='btn2')
set3 = InlineKeyboardButton('3', callback_data='btn3')
menuAdmin.add(set1,set2,set3)

menuBack = InlineKeyboardMarkup(row_width=1)

back = InlineKeyboardButton('Ortga', callback_data='btn0')
menuBack.add(back)