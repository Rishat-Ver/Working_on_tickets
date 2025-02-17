from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import  CallbackQuery
from sqlalchemy import select
from dotenv import load_dotenv

import os

from database.db import Ticket, Profession, SessionLocal
from handlers.state import AddTicketState
from keyboards.inline_keyboards import get_professions_keyboard
from filters.checkers import check_message_new_task


router_add_task = Router()

load_dotenv()

PROFESSIONS = ['DA','DE','DS','DEV']

@router_add_task.message(lambda message: message.text == "New Task")
async def cmd_add_ticket(message: Message, state: FSMContext):

    await state.set_state(AddTicketState.waiting_for_keys_hour)
    await message.reply("✍️\nТаска\nЧасы\nСсылка*")


@router_add_task.message(AddTicketState.waiting_for_keys_hour)
async def process_keys_hour(message: Message, state: FSMContext):

    if not await check_message_new_task(message):
        return

    args = message.text.split('\n')
    if len(args) == 3:
        keys, hour, link = args[0], args[1], args[2]
    else:
        keys, hour, link = args[0], args[1], ''

    await state.update_data(keys=keys, hour=int(hour), link=link)

    await state.set_state(AddTicketState.waiting_for_profession)

    professions_keyboard = await get_professions_keyboard()

    await message.reply("📋 Выбери профессию:", reply_markup=professions_keyboard)


@router_add_task.callback_query(lambda c: c.data in os.getenv('PROFESSIONS').split(','))
async def process_profession_selection(callback: CallbackQuery, state: FSMContext):

    profession_name = callback.data

    async with SessionLocal() as session:
        result = await session.execute(select(Profession).where(Profession.name == profession_name))
        profession = result.scalar()

        if not profession:
            await callback.message.edit_text("❌ Такой профессии нет. ❌")
            await state.clear()
            return

        data = await state.get_data()
        keys = data['keys']
        hour = data['hour']
        link = data['link']

        new_task = Ticket(keys=keys, link=link, hour=hour, profession_id=profession.id)
        session.add(new_task)
        await session.commit()

    await callback.message.edit_text(f"✅\nТаска: {keys} добавлена")
    await state.clear()


def register_handlers_add_task(dp):
    dp.include_router(router_add_task)