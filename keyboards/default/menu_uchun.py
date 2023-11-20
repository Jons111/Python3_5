from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Taomlar"),
            KeyboardButton(text="Ichimliklar"),
        ],
        [
            KeyboardButton(text="Shirinliklar"),
            KeyboardButton(text="Fast food")
        ],
        [
            KeyboardButton(text="Lokatsiya",request_location=True),
            KeyboardButton(text="Kontakt",request_contact=True)
        ],
        [
            KeyboardButton(text="adminga murojat")
        ]
    ],
    resize_keyboard=True
)