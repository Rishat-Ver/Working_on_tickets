from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from filters.checkers import check_user_id
from keyboards.standart_keyboards import main_keyboard

router_start = Router()


@router_start.message(Command(commands='start'))
async def send_keyboard(message: Message):

    if not await check_user_id(message):
        return
    await message.answer("Добро пожаловать !", reply_markup=main_keyboard)


def register_handlers_start(dp):
    dp.include_router(router_start)