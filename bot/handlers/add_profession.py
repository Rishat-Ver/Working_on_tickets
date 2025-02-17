from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from sqlalchemy import select

from database.db import Profession, SessionLocal
from filters.checkers import check_proffesion
from handlers.state import AddProfessionState
from keyboards.inline_keyboards import generate_keybords_professions


router_add_profession = Router()


@router_add_profession.message(Command("add_profession"))
async def add_profession(message: Message, state: FSMContext):

    await state.set_state(AddProfessionState.waiting_for_profession_name)
    await message.reply("✍️ Введи название профессии:")


@router_add_profession.message(AddProfessionState.waiting_for_profession_name)
async def process_profession_name(message: Message, state: FSMContext):

    if not await check_proffesion(message):
        return

    profession_name = message.text.split()[0]

    async with SessionLocal() as session:
        result = await session.execute(select(Profession).where(Profession.name == profession_name))
        existing_profession = result.scalar()

        if existing_profession:
            await message.reply("⚠️ Такая профессия уже есть в базе!")
            return

        new_profession = Profession(name=profession_name)
        session.add(new_profession)
        await session.commit()

    generate_keybords_professions(profession_name)

    await message.reply(f"✅ Профессия '{profession_name}' добавлена!")
    await state.clear()


def register_handlers_add_profession(dp):
    dp.include_router(router_add_profession)