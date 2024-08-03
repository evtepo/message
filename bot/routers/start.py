from aiogram import Bot, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, BotCommandScopeDefault

router = Router(name=__name__)


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(f"Hello, {message.from_user.full_name}. Use /menu to see all commands.")


@router.message(Command("menu"))
async def menu_command(message: Message, bot: Bot):
    commands = await bot.get_my_commands(scope=BotCommandScopeDefault())
    response = "Available commands:\n"
    for command in commands:
        response += f"/{command.command} - {command.description}\n"

    await message.answer(response)
