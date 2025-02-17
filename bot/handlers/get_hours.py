from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import  CallbackQuery
from aiogram.types import Message
from sqlalchemy import select, func

import datetime
from database.db import Ticket, Profession, SessionLocal
from handlers.state import GetHoursState
from filters.checkers import check_date
from datetime import timedelta
from utils.mode_date import format_date


router_get_hours = Router()


@router_get_hours.message(lambda message: message.text == "Get Hour")
async def callback_get_hours(message: Message, state: FSMContext):

    await state.set_state(GetHoursState.waiting_for_start_date)
    await message.reply("📅\nВведите дату:")


@router_get_hours.message(GetHoursState.waiting_for_start_date)
async def process_start_date(message: Message, state: FSMContext):

    start_date = await check_date(message)

    if not start_date:
        return

    today = datetime.date.today() - timedelta(days=1)

    async with SessionLocal() as session:
        result = await session.execute(
            select(Profession.name, func.sum(Ticket.hour))
            .join(Ticket)
            .where(Ticket.date >= start_date)
            .where(Ticket.date <= today)
            .group_by(Profession.name)
        )
        hours_by_profession = result.fetchall()

    if not hours_by_profession:
        await message.reply(f"Нет часов за этот период")
    else:
        response = f"🕓С {format_date(start_date)} по {format_date(today)}:🕓\n\n"
        all_hours = 0
        for profession, hours in hours_by_profession:
            response += f"{profession}: <b>{hours}</b> часов\n"
            all_hours += hours
        response += f"\nОбщие часы: <b>{all_hours}</b> часов"

        await message.answer(response, parse_mode="HTML")

    await state.clear()


def register_handlers_get_hours(dp):
    dp.include_router(router_get_hours)