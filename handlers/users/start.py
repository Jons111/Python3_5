from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from keyboards.default.menu_uchun import menu_buttons
from keyboards.default.toamlar_uchun import taomlar_buttons
from keyboards.inline.tillar_uchun import tillar_buttons
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=tillar_buttons)


@dp.callback_query_handler(text="til1")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"Assalomu alaykum botga hush kelibsiz",reply_markup=menu_buttons )

@dp.message_handler(text='Taomlar')
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum botga hush kelibsiz",reply_markup=taomlar_buttons)