from aiogram.types import Message, ContentType, InputFile
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import FSMContext
from loader import dp, bot

from data.config import ADMIN_CHANNEL, ADMINS

import cloudinary
import cloudinary.uploader
import cloudinary.api
import pathlib


@dp.message_handler(IsUserPictureNumberFilter(), content_types=ContentType.PHOTO)
async def change_bg(message: Message):
    pass
