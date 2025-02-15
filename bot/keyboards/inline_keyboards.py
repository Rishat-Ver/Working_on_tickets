from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


button_1 = InlineKeyboardButton(text='DA', callback_data='DA')
button_2 = InlineKeyboardButton(text='DS', callback_data='DS')
button_3 = InlineKeyboardButton(text='DE', callback_data='DE')
button_4 = InlineKeyboardButton(text='DEV', callback_data='DEV')

professions_keyboard =InlineKeyboardMarkup(
    inline_keyboard=[[button_1, button_2, button_3, button_4]]
)