from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message
from keyboards.inline.post import menu
from loader import dp, bot
from states.personalData import PersonalData
from utils.misc.models import *
from data.config import ADMINS


@dp.message_handler(Command('anketa'))
async def select_category(message: types.Message):
    if not Blocked.user_exists(message.chat.id):
        await message.answer(f"Qaysi yo`nalishda ro`yxatdan o`tmoqchisiz?\n          👦bolalar yoki kattalar👨‍🎓")
        await PersonalData.fullName.set()
    else:
        await message.answer(
            "Siz oldin anketa to'ldirgansiz. Yana to'ldirish uchun admin @ashuroff_dev ga murojaat eting.")


@dp.message_handler(state=PersonalData.fullName)
async def select_category(message: types.Message, state=FSMContext):
    fullname = message.text

    await state.update_data({'name': fullname})

    await message.answer('To`liq ismingizni kiritng (FISH):')
    await PersonalData.next()


@dp.message_handler(state=PersonalData.email)
async def select_category(message: types.Message, state=FSMContext):
    email = message.text

    await state.update_data({'email': email})

    await message.answer('Telefon  raqamingizni kiriting (+998 bilan): ')

    await PersonalData.next()


@dp.message_handler(state=PersonalData.phoneNum)
async def select_category(message: types.Message, state=FSMContext):
    num = message.text

    await state.update_data({'phone': num})

    data = await state.get_data()
    name = data.get("name")
    email = data.get("email")
    num = data.get("phone")

    msgs = f'Quyidagi ma`lumotlar qabul qilindi: \n '
    msg = f'Yo`nalishingiz - {name}\n'
    msg += f'Ism Familiyangiz - {email}\n'
    msg += f'Telefon raqamingiz - {num}'

    global user
    user = f"<b>Foydalanuvchi, {message.from_user.get_mention()} anketa to'ldirdi.</b>\n{msg}"

    await message.answer(msgs)
    await message.answer(msg, reply_markup=menu)

    await state.finish()


@dp.callback_query_handler(text='tasdiq')
async def select_tasdiq(call: CallbackQuery):
    await bot.send_message(-1001625418637, user)
    await call.message.edit_text("✅Tasdiqlandi. Siz bilan tez orada bog`lanamiz📞"
                                 "\nyoki biz bilan bog`laning⤵️\n +998931790214 \n+998943066003 \n"
                                 "〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️"
                                 "\nBizning markaz:"
                                 "\n📍Namangan viloyati, Yangiqo'rg'on tumani \nMo'ljal: Prokrotura "
                                 f"yonida")


@dp.callback_query_handler(text='rad')
async def select_rad(call: CallbackQuery):
    await call.message.edit_text("❌Rad etildi. Qayta ♻️to`ldirish uchun /anketa buyrug`ini yuboring")
