import logging
import time
from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.fsm.context import FSMContext
from aiogram.types import TelegramObject, Message

logger = logging.getLogger(__name__)


class CounterMiddleware(BaseMiddleware):

    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]],
                                         Awaitable[Any]], event: Message,
                       data: Dict[str, Any]) -> Any:
        result = await handler(event, data)

        state: FSMContext = data["state"]
        state_data = await state.get_data()

        if "counter" not in state_data:
            await state.update_data({"counter": 1})
        else:
            await state.update_data({"counter": state_data["counter"] + 1})
        state = await state.get_data()
        
        await event.answer(f"Отправлено сообщений: {state_data['counter']}")

        return result
