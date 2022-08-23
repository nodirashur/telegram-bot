from aiogram import types
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BotBlocked as bb

from loader import dp, bot

from states.personalData import PersonalData
from data.config import ADMINS
from utils.misc.models import *
from keyboards.inline.adminKeyboards import menuAdmin, menuBack


@dp.message_handler(Command("admin", prefixes="!"), user_id=ADMINS)
async def panel(m: types.Message):
    await m.answer("<b>Kerakli buyruqni tanlang:\n1. Foydalanuvchiga yana 1 marta anketa to'ldirish uchun ruxsat "
                   "berish.\n2. Bot a'zolari.\n3. A'zolarga xabar yuborish.</b>", reply_markup=menuAdmin)


@dp.callback_query_handler(user_id=ADMINS)
async def panel(call: CallbackQuery):
    data = call.data
    if data == 'btn0':
        await call.message.edit_text("<b>Kerakli buyruqni tanlang:\n1. Foydalanuvchiga yana 1 marta anketa to'ldirish "
                                     "uchun ruxsat berish.\n2. Bot a'zolari.\n3. A'zolarga xabar yuborish.</b>",
                                     reply_markup=menuAdmin)
    if data == 'btn1':
        await PersonalData.unban.set()
        await call.message.edit_text("<b>Foydalanuvchi IDsini kiriting.</b>", reply_markup=menuBack)
    if data == 'btn2':
        users_count = len(Users.select())
        blocked_count = len(Blocked.select())
        await call.answer(f"Bot a'zolari: {users_count} ta.\nAnketa to'ldirganlar {blocked_count} ta.", show_alert=True)
    if data == 'btn3':
        await call.message.edit_text("<b>Xabar yuborish uchun xabaringizni kiriting.</b>", reply_markup=menuBack)
        await PersonalData.sendMsg.set()


@dp.message_handler(user_id=ADMINS, state=PersonalData.unban)
async def panel(m: Message, state: FSMContext):
    msg = m.text
    try:
        user = f'<a href="tg://user?id={msg}">{msg}</a>'
        await m.delete()
        await m.answer(f"<b>Foydalanuvchi {user} yana anketa to'ldirishi mumkin.</b>", reply_markup=menuBack)
        Blocked.delete_user(msg)
        await bot.send_message(msg, "<b>Admin sizni yana bir marta anketa to'ldirishingizga ruxsat berdi!</b>")
        await state.finish()
    except:
        await m.answer("<s>Foydalanuvchi IDsi noto'g'ri yozilgan!</s>", reply_markup=menuBack)
        await state.finish()


@dp.message_handler(user_id=ADMINS, state=PersonalData.sendMsg)
async def panel(m: Message, state: FSMContext):
    msg = m.text
    b = 0
    i = 0
    for user in Users.select():
        try:
            await bot.send_message(user.user_id, msg)
            i += 1
        except bb:
            b += 1
    await m.answer(f"<b>Xabaringiz {i} ta bot a'zolariga yuborildi.\n{b} ta a'zolarga yuborilmadi</b>",
                   reply_markup=menuBack)
    await state.finish()
