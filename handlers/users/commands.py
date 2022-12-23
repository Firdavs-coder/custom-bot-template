from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp
from loader import dp
from data.config import ADMINS


@dp.message_handler(CommandStart(), chat_id=ADMINS)
async def bot_admin_start(message: types.Message):
    await message.answer(f"😎 Assalomu alaykum admin janoblari.")


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, botimizga xush kelibsiz!\nFoydalanish uchun bo'limni tanlang.")


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer(f"Botdagi nosozliklar yoki kamchiliklarni admin yuborishingiz mumkin. \n\nAdmin - @shavkatNor")
