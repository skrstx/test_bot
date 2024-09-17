from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

commands_router = Router()

@commands_router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(f"Hello, {message.from_user.first_name}!")

@commands_router.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer("Этот бот не умеет нихуя")