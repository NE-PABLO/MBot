import os
from aiogram import F
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile

from handlers import router

from twoversion.config import BASE_IMAGE_PATH # Импортируем путь к папке с изображениями 


# --------------------- Формулы равномерного движения по окружности -----------------завершено
async def send_ravn_dvizh_po_okruzhnosti_formula(message: Message, filename: str, caption: str):
    try:
        image_path = os.path.join(
            BASE_IMAGE_PATH,
            "Механика",
            "Кинематика",
            "Равномерное движение по окружности",
            filename
        )
        photo = FSInputFile(image_path)
        await message.answer_photo(photo, caption=caption)
    except Exception as e:
        await message.answer(f"⚠️ Ошибка загрузки формулы: {str(e)}")

@router.message(F.text == "Скорость при равномерном движении по окружности")
async def send_skorost_ravn_dvizh_po_okruzhnosti_handler(message: Message):
    await send_ravn_dvizh_po_okruzhnosti_formula(message,
                              "Скорость_при_равномерном_движении_по_окружности.jpg",
                              "Формула скорости при равномерном движении по окружности")

@router.message(F.text == "Формула связи периода и частоты")
async def send_formula_svyazi_perioda_i_chastoty_handler(message: Message):
    await send_ravn_dvizh_po_okruzhnosti_formula(message,
                              "Формула_связи_периода_и_частоты.jpg",
                              "Формула связи периода и частоты")

@router.message(F.text == "Центростремительное ускорение")
async def send_centrostremitelnoe_uskorenie_handler(message: Message):
    await send_ravn_dvizh_po_okruzhnosti_formula(message,
                              "Центростремительное_ускорение.jpg",
                              "Формула центростремительного ускорения")

@router.message(F.text == "Угловая скорость")
async def send_uglovoe_skorost_handler(message: Message):
    await send_ravn_dvizh_po_okruzhnosti_formula(message,
                              "Угловая_скорость.jpg",
                              "Формула углового ускорения")