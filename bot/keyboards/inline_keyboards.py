from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from sqlalchemy import select
from database.db import SessionLocal, Profession


async def get_professions_keyboard() -> InlineKeyboardMarkup:

    async with SessionLocal() as session:
        result = await session.execute(select(Profession.name))
        professions = [row[0] for row in result.fetchall()]

    if not professions:
        return None

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=prof, callback_data=prof)] for prof in professions])

    return keyboard
