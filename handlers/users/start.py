from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from utils.misc.models import Users


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if not Users.user_exists(message.chat.id):
        Users.create_user(message.chat.id)
    text = (f"<b>👋️Salom {message.from_user.get_mention()} , <a href='https://t.me/+RaYUc1Ng_OPfeKo-'>Foxford</a> "
            f" rasmiy botiga xush kelibsiz"
            f"\n /anketa buyrug'ini yuboring va ro`yxatdan o`ting!\n\nYordam va ma'lumot uchun "
            f"/help buyrug'ini yuboring.</b>\n〰️〰️〰️〰️〰️〰️〰️〰️〰〰️〰️〰️〰️〰️〰️〰️〰️〰\n"
            f"<b>Bizning markaz: \n <i>📍Namangan viloyati, Yangiqo'rg'on tumani</i> \nMo'ljal: <i>Prokrotura "
            f"yonida</i></b>")
    await message.answer(text)
