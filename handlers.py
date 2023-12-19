from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Hello, world!")


@router.message(F.text == 'Test')
async def filtered_message_handler(msg: Message):
    await msg.answer("Test")


@router.message(F.content_type.in_({'photo'}))
async def photo_handler(msg: Message):
    await msg.answer("Thanks for your photo!")


@router.message()
async def message_handler(msg: Message):
    await msg.answer("By this time i can't answer for this type of messages")
