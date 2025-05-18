import os
from aiogram import F
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile

from handlers import router

from twoversion.config import BASE_IMAGE_PATH # Импортируем путь к папке с изображениями 

# --------------------- Формулы Законы постоянного тока -----------------
async def send_postoyanniy_tok_formula(message: Message, filename: str, caption: str):
    try:
        image_path = os.path.join(
            BASE_IMAGE_PATH,
            "Электродинамика",
            "Законы постоянного тока",
            filename
        )
        photo = FSInputFile(image_path)
        await message.answer_photo(photo, caption=caption)
    except Exception as e:
        await message.answer(f"⚠️ Ошибка загрузки формулы: {str(e)}")

@router.message(F.text == "Сила тока")
async def sila_toka_handler(message: Message):
    await send_postoyanniy_tok_formula(message,
                              "Сила_тока.jpg",
                              "Формула силы тока")
    
@router.message(F.text == "Электрическое сопротивление")
async def electric_soprotivlenie_handler(message: Message):
    await send_postoyanniy_tok_formula(message,
                              "Электрическое_сопротивление.jpg",
                              "Формула электрического сопротивления")
    
@router.message(F.text == "Закон Ома")
async def zakon_oma_handler(message: Message):
    await send_postoyanniy_tok_formula(message,
                              "Закон_Ома.jpg",
                              "Формула закона Ома")
    
@router.message(F.text == "Последовательное соединение проводников")
async def posledovatelnoe_soedinenie_provodnikov_handler(message: Message):
    await send_postoyanniy_tok_formula(message,
                              "Последовательное_соединение_проводников.jpg",
                              "Формула последовательного соединения проводников")
    
@router.message(F.text == "Параллельное соединение проводников")
async def parallelnoe_soedinenie_provodnikov_handler(message: Message):
    await send_postoyanniy_tok_formula(message,
                              "Параллельное_соединение_проводников.jpg",
                              "Формула параллельного соединения проводников")
    
@router.message(F.text == "Работа электрического тока")
async def rabota_electric_toka_handler(message: Message):
    await send_postoyanniy_tok_formula(message,
                              "Работа_электрического_тока.jpg",
                              "Формула работы электрического тока")
    
@router.message(F.text == "Закон Джоуля-Ленца")
async def zakon_joulya_lenca_handler(message: Message):
    await send_postoyanniy_tok_formula(message,
                              "Закон_Джоуля-Ленца.jpg",
                              "Формула закона Джоуля-Ленца")
    
@router.message(F.text == "Мощность тока")
async def moshnost_toka_handler(message: Message):
    await send_postoyanniy_tok_formula(message,
                              "Мощность_тока.jpg",
                              "Формула мощности тока")