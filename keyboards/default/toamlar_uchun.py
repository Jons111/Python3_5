from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

taomlar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Osh"),
            KeyboardButton(text="Lag'mon")
        ],
        [
            KeyboardButton(text="Sho'rva")
        ],
        [
            KeyboardButton(text="Kabob"),
            KeyboardButton(text="Somsa")
        ]
    ],
    resize_keyboard=True
)


tasdiqlash_buttons =ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="tasdiqlash"),
            KeyboardButton(text="bekor qilish")
        ]
    ],
    resize_keyboard=True
)