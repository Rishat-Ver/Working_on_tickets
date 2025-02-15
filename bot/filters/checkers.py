from aiogram.types import Message
from dotenv import load_dotenv

import os


load_dotenv()


async def check_user_id(message: Message):
    if message.from_user.id != int(os.getenv('MY_ID')):
        await message.reply("❌ У тебя нет доступа к этому боту. ❌")
        return False
    return True


async def check_proffesion(message: Message):
    profession = message.text.split()
    if len(profession) > 1:
        await message.reply("❌ Укажи только одну профессию. ❌")
        return False
    if profession[0] not in os.getenv("PROFESSIONS", "").split(","):
        await message.reply("❌ Нет такой профессии. ❌")
        return False
    return True


async def check_message_new_task(message: Message):
    args = message.text.split('\n')
    if len(args) not in [2, 3]:
        await message.reply("❌ Нужно ввести задачу, часы, ссылку ❌")
        return False
    if not args[1].isdigit():
        await message.reply("❌ Часы должны быть числом. ❌")
        return False
    return True
