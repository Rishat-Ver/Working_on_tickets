from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from dotenv import load_dotenv

import asyncio
import os
from handlers import start, add_profession
from database.db import init_db


load_dotenv()


bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()

start.register_handlers_start(dp)
add_profession.register_handlers_add_profession(dp)


async def set_main_menu(bot: Bot):

    commands = [
        BotCommand(command="start", description="Начать работу с ботом"),
        BotCommand(command="add_profession", description="Добавить профессию"),
    ]
    await bot.set_my_commands(commands)


async def main():
    await set_main_menu(bot)
    await init_db()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
