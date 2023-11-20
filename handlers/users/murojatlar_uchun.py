from aiogram import types
from aiogram.dispatcher import FSMContext
from states.holatlar import Forma
from loader import dp,bot



@dp.message_handler(text="adminga murojat")
async def bot_echo(message: types.Message):

    await message.answer(text="ismni kiriting")
    await Forma.ism_qabul_qilish.set()


@dp.message_handler(state= Forma.ism_qabul_qilish)
async def bot_echo(message: types.message,state:FSMContext):
    ism =message.text
    await state.update_data({"name":ism})
    await message.answer(text="ism kiriting")
    await Forma.familya_qabul_qilish().set()


@dp.message_handler(state= Forma.familya_qabul_qilish)
async def bot_echo(message: types.message,state:FSMContext):
    familya =message.text
    await state.update_data({"fam":familya})
    await message.answer(text="familyani kiriting")
    await Forma.yosh_qabul_qilish().set()


@dp.message_handler(state=Forma.yosh_qabul_qilish)
async def bot_echo(message: types.message, state: FSMContext):
    yosh = message.text
    await state.update_data({"yoh":yosh})
    await message.answer(text="yosh kiriting")
    await Forma.tel_qabul_qilish().set()

@dp.message_handler(state=Forma.tel_qabul_qilish)
async def bot_echo(message: types.message, state: FSMContext):
    tel = message.text
    await state.update_data({"tell":tel})
    await message.answer(text="tel kiriting")
    await Forma.murojat_qabul_qilish().set()

@dp.message_handler(state=Forma.murojat_qabul_qilish)
async def bot_echo(message: types.message, state: FSMContext):

    malumot = message.text
    await state.update_data({'text':malumot})

    malumot_olish = await state.get_data()
    user_ismi = malumot_olish.get('name')
    user_familya = malumot_olish.get('familya')
    user_yosh = malumot_olish.get('yosh')
    user_tel = malumot_olish.get('tel')
    user_murojat = malumot_olish.get('text')
    math = f"Ism :{user_ismi} \n" \
           f"familya :{user_familya} \n" \
           f"yosh :{user_yosh} \n" \
           f"tel :{user_tel} \n" \
           f"murojat : \n\n{user_murojat} "
    user_id = message.from_user.id
    await bot.send_message(chat_id= user_id,text=math)
    await Forma.familya_qabul_qilish.set()


@dp.message_handler(state=Forma.tasdiqlash_qabul_qilish,text="bekor qilish")
async def bot_echo(message: types.message, state: FSMContext):

    await message.answer(text="bekor qilindi")
    await state.finish()



@dp.message_handler(state=Forma.tasdiqlash_qabul_qilish,text="tasdiqlash")
async def bot_echo(message: types.message, state: FSMContext):
    malumat_olish = await state.get_data()
    user_ismi =malumat_olish.get('name')
    user_familya =malumat_olish.get('familya')
    user_yosh =malumat_olish.get('yosh')
    user_tel =malumat_olish.get('tel')
    user_murojat =malumat_olish.get('text')
    username = message.from_user.username
    math = f"Ushbu foydalanuvchi {username}\n" \
           f"Ism :{user_ismi} \n" \
           f"familya :{user_familya} \n" \
           f"yosh :{user_yosh} \n" \
           f"tel :{user_tel} \n" \
           f"murojat : \n\n{user_murojat}"
    await bot.send_message(chat_id='6570924683',text=math)
    await state.finish()






