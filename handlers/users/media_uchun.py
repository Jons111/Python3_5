from aiogram import types
from aiogram.types import ContentType, InputFile

from loader import dp,bot


# Echo bot
@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()
    await message.answer(text="Dakument saqlab olindi")

@dp.message_handler(content_types=ContentType.VIDEO)
async def bot_echo(message: types.Message):
    await message.video.download()
    await message.answer(text="Vidoe saqlab olindi")

@dp.message_handler(content_types=ContentType.PHOTO)
async def bot_echo(message: types.Message):
    await message.photo[-1].download()
    await message.answer(text="Rasm saqlab olindi")

@dp.message_handler(text="Osh")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/UstozShogird/25032"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu osh")
























