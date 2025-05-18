import os
from aiogram import Router, F
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile

from handlers import router

from twoversion.config import BASE_IMAGE_PATH # Импортируем путь к папке с изображениями 

# --------------------- Формулы Оптика -----------------
async def send_optics_formula(message: Message, filename: str, caption: str):
    try:
        image_path = os.path.join(
            BASE_IMAGE_PATH,
            "Оптика",
            filename
        )
        photo = FSInputFile(image_path)
        await message.answer_photo(photo, caption=caption)
    except Exception as e:
        await message.answer(f"⚠️ Ошибка загрузки формулы: {str(e)}")

@router.message(F.text == "Закон прямолинейного распространения света")
async def zakon_prjamolinejnogo_rasprostranenija_sveta_handler(message: Message):
    await send_optics_formula(message,
                              "Закон_прямолинейного_распространения_света.jpg",
                              "Понятие 'Закон прямолинейного распространения света'")
    
@router.message(F.text == "Закон отражения света")
async def zakon_otrazhenija_sveta_handler(message: Message):
    await send_optics_formula(message,
                              "Закон_отражения_света.jpg",
                              "Понятие 'Закон отражения света'")
    
@router.message(F.text == "Закон преломления света")
async def zakon_prelomlenija_sveta_handler(message: Message):
    await send_optics_formula(message,
                              "Закон_преломления_света.jpg",
                              "Понятие 'Закон преломления света'")
    
@router.message(F.text == "Оптическая сила линзы")
async def opticheskaja_sila_linzy_handler(message: Message):
    await send_optics_formula(message,
                              "Оптическая_сила_линзы.jpg",
                              "Формула 'Оптическая сила линзы'")
    
@router.message(F.text == "Формула линзы")
async def formula_linzy_handler(message: Message):
    await send_optics_formula(message,
                              "Формула_линзы.jpg",
                              "Формула 'Формула линзы'")
    
@router.message(F.text == "Интерференция света")
async def interferencija_sveta_handler(message: Message):
    await send_optics_formula(message,
                              "Интерференция_света.jpg",
                              "Формула 'Интерференция света'")
    
@router.message(F.text == "Формула дифракционной решетки")
async def formula_difrakcionnoj_reschetki_handler(message: Message):
    await send_optics_formula(message,
                              "Формула_дифракционной_решетки.jpg",
                              "Формула 'Формула дифракционной решетки'")