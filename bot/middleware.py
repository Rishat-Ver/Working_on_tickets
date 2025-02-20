from aiogram.types import Message, CallbackQuery, Update
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from typing import Callable, Dict, Any, Awaitable
from dotenv import load_dotenv

import os
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

load_dotenv()

MY_ID = int(os.getenv("MY_ID"))


class AccessMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any]
    ) -> Any:
        user_id = None

        if isinstance(event, Message):
            user_id = event.from_user.id
        elif isinstance(event, CallbackQuery):
            user_id = event.from_user.id

        if user_id and user_id != MY_ID:
            if isinstance(event, Message):
                await event.answer("⛔️ Доступ запрещён.")
            elif isinstance(event, CallbackQuery):
                await event.answer("⛔️ Доступ запрещён.", show_alert=True)
            return

        return await handler(event, data)