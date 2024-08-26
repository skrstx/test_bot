import logging
import asyncio

from aiogram import Dispatcher, Bot
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers.commands import commands_router
from handlers.other import other_router

from config_data.config import load_config, Config

logging.basicConfig(
    level=logging.DEBUG,
    format="[{asctime}] #{levelname} {filename}:{lineno} - {name} - {message}",
    style="{")

logger = logging.getLogger(__name__)


async def main() -> None:
    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    
    dp.include_router(commands_router)
    dp.include_router(other_router)
    
    await dp.start_polling(bot)


asyncio.run(main())
