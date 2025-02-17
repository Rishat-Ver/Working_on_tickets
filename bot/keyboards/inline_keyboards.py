from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


PROFESSIONS = ['DA', 'DS', 'DE', 'DEV']

professions_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[]]
)

def generate_keybords_professions(new_prof):

    PROFESSIONS.append(new_prof)

    for i in range(len(PROFESSIONS)):
        button = InlineKeyboardButton(text=PROFESSIONS[i], callback_data=PROFESSIONS[i])
        if len(professions_keyboard.inline_keyboard[-1]) < 4:
            professions_keyboard.inline_keyboard[-1].append(button)
        else:
            professions_keyboard.inline_keyboard.append([button])
