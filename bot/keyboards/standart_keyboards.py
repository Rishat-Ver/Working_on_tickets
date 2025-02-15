from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_1 = KeyboardButton(text="New Task")

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [button_1],
    ],
    resize_keyboard=True
)