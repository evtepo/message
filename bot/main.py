import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand, BotCommandScopeDefault

from config.settings import settings
from routers.message import router as message_router
from routers.start import router as start_router


dp = Dispatcher(storage=MemoryStorage())


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Beginning of work"),
        BotCommand(command="write", description="Create a message"),
        BotCommand(command="messages", description="List of messages"),
        BotCommand(command="menu", description="Show all commands"),
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())


dp.include_router(message_router)
dp.include_router(start_router)


async def main():
    bot = Bot(
        token=settings.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    await set_commands(bot)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
