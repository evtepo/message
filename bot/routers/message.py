from http import HTTPStatus

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from aiohttp import ClientSession
from textwrap import dedent

from config.settings import settings


router = Router(name=__name__)


class MessageForm(StatesGroup):
    waiting_for_message = State()


@router.message(Command("write"))
async def write_message(message: Message, state: FSMContext):
    await message.answer("Please write your message:")
    await state.set_state(MessageForm.waiting_for_message)


@router.message(MessageForm.waiting_for_message)
async def process_message(message: Message, state: FSMContext):
    data = {
        "author": message.from_user.full_name,
        "text": message.text,
    }

    async with ClientSession() as session:
        try:
            async with session.post(settings.api_url, json=data) as response:
                if response.status == HTTPStatus.CREATED:
                    await message.answer("Message created successfully.")
                else:
                    await message.answer("Something went wrong. Please try again.")
        except Exception as e:
            await message.answer(f"An error occurred: {type(e).__name__}")
        finally:
            await state.clear()


class PaginationForm(StatesGroup):
    waiting_for_pagination = State()


@router.message(Command("messages"))
async def get_messages(message: Message, state: FSMContext):
    text = dedent(
        """
        Please provide the page number and
        page size separated by a space.
        Example: 1 10
        """
    )
    await message.answer(text)
    await state.set_state(PaginationForm.waiting_for_pagination)


@router.message(PaginationForm.waiting_for_pagination)
async def process_pagination(message: Message, state: FSMContext):
    async with ClientSession() as session:
        try:
            page, size = map(int, message.text.split())
            params = {"page": page, "size": size}
            async with session.get(settings.api_url, params=params) as response:
                if response.status == HTTPStatus.OK:
                    response = await response.json(encoding="utf-8")

                    pages = response.get("links", {})
                    messages = response.get("data", [])

                    if not messages:
                        await message.answer("No messages found.")
                    else:
                        prev_page = pages.get("prev")
                        next_page = pages.get("next")
                        pages = f"Previous page: {prev_page}\nNext page: {next_page}\n\n"
                        messages = ",\n".join([f"{message}" for message in messages])

                        await message.answer(f"{pages}Messages:\n{messages}")
                else:
                    await message.answer("Something went wrong. Please try again.")
        except Exception as e:
            await message.answer(f"An error occurred: {type(e).__name__}")
        finally:
            await state.clear()
