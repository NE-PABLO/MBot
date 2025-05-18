import os
from aiogram import F
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile

from handlers import router

from twoversion.config import BASE_IMAGE_PATH # Импортируем путь к папке с изображениями

# --------------------- Формула средней скорости -----------------завершено
async def send_srednaa_skorost_formula(message: Message, filename: str, caption: str):
    try:
        image_path = os.path.join(
            BASE_IMAGE_PATH,
            "Механика",
            "Кинематика",
            filename
        )
        photo = FSInputFile(image_path)
        await message.answer_photo(photo, caption=caption)
    except Exception as e:
        await message.answer(f"⚠️ Ошибка загрузки формулы: {str(e)}")

@router.message(F.text == "Средняя скорость")
async def send_srednaa_skorost_handler(message: Message):
    await send_srednaa_skorost_formula(message,
                              "Средняя_скорость.jpg",
                              "Формула средней скорости")