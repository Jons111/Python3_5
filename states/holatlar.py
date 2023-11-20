from aiogram.dispatcher.filters.state import State, StatesGroup

class Forma(StatesGroup):
    ism_qabul_qilish= State()
    familya_qabul_qilish= State()
    yosh_qabul_qilish= State()
    tel_qabul_qilish= State()
    murojat_qabul_qilish = State()
    tasdiqlash_qabul_qilish= State()