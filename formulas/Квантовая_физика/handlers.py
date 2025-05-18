import os
from aiogram import F
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile

from handlers import router

from twoversion.config import BASE_IMAGE_PATH # Импортируем путь к папке с изображениями 

# --------------------- Формулы Квантовая физика -----------------
async def send_quantum_physics_formula(message: Message, filename: str, caption: str):
    try:
        image_path = os.path.join(
            BASE_IMAGE_PATH,
            "Квантовая физика",
            filename
        )
        photo = FSInputFile(image_path)
        await message.answer_photo(photo, caption=caption)
    except Exception as e:
        await message.answer(f"⚠️ Ошибка загрузки формулы: {str(e)}")

@router.message(F.text == "Формула Планка")
async def formula_planka_handler(message: Message):
    await send_quantum_physics_formula(message,
                              "Формула_Планка.jpg",
                              "Формула Планка")
    
@router.message(F.text == "Энергия фотона")
async def energiya_fotona_handler(message: Message):
    await send_quantum_physics_formula(message,
                              "Энергия_фотона.jpg",
                              "Формула Энергия фотона")
    
@router.message(F.text == "Импульс фотона")
async def impulc_fotona_handler(message: Message):
    await send_quantum_physics_formula(message,
                              "Импульс_фотона.jpg",
                              "Формула Импульс фотона")
    
@router.message(F.text == "Уравнение Эйнштейна для фотоэффекта")
async def uravnenie_einsteina_dlya_fotoeffekta_handler(message: Message):
    await send_quantum_physics_formula(message,
                              "Уравнение_Эйнштейна_для_фотоэффекта.jpg",
                              "Формула Уравнение Эйнштейна для фотоэффекта")