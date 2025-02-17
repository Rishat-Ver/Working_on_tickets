from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_1 = KeyboardButton(text="New Task")
button_2 = KeyboardButton(text="Get Hours")

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [button_1, button_2],
    ],
    resize_keyboard=True
)