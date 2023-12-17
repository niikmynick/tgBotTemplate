from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from filters import TextFilter

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("ksrhka")


@router.message()
async def message_handler(msg: Message):
    await msg.answer("")


@router.message(TextFilter("Задачи"))
async def filtered_message_handler(msg: Message):
    await msg.answer("")
