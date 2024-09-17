from aiogram import Router
from aiogram.types import Message

other_router = Router()


@other_router.message()
async def send_echo(message: Message):
    await message.send_copy(chat_id=message.from_user.id)
