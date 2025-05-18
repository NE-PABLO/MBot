import os
from aiogram import F
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile

from handlers import router

from twoversion.config import BASE_IMAGE_PATH # Импортируем путь к папке с изображениями 


# --------------------- Формулы Электромагнитные колебания и волны -----------------
async def send_electromagnetic_oscillations_formula(message: Message, filename: str, caption: str):
    try:
        image_path = os.path.join(
            BASE_IMAGE_PATH,
            "Электродинамика",
            "Электромагнитные колебания и волны",
            filename
        )
        photo = FSInputFile(image_path)
        await message.answer_photo(photo, caption=caption)
    except Exception as e:
        await message.answer(f"⚠️ Ошибка загрузки формулы: {str(e)}")

@router.message(F.text == "Колебательный контур")
async def kolebatelniy_kontur_handler(message: Message):
    await send_electromagnetic_oscillations_formula(message,
                              "Колебательный_контур.jpg",
                              "Понятие 'Колебательный контур'")
    
@router.message(F.text == "Уравнения колебаний в колебательном контуре")
async def uravneniya_kolebanii_v_kolebatelnom_konture_handler(message: Message):
    await send_electromagnetic_oscillations_formula(message,
                              "Уравнения_колебаний_в_колебательном_контуре.jpg",
                              "Формула уравнений колебаний в колебательном контуре")
    
@router.message(F.text == "Формула Томсона")
async def formula_tomsona_handler(message: Message):
    await send_electromagnetic_oscillations_formula(message,
                              "Формула_Томсона.jpg",
                              "Формула Томсона")
    
@router.message(F.text == "Закон сохранения энергии в контуре")
async def zakon_sohraneniya_energii_v_konture_handler(message: Message):
    await send_electromagnetic_oscillations_formula(message,
                              "Закон_сохранения_энергии_в_контуре.jpg",
                              "Формула закона сохранения энергии в контуре")
    
@router.message(F.text == "Шкала электромагнитных волн")
async def shkala_electromagnitnih_voln_handler(message: Message):
    await send_electromagnetic_oscillations_formula(message,
                              "Шкала_электромагнитных_волн.jpg",
                              "Понятие 'Шкала электромагнитных волн'")
