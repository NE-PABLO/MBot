import os
from aiogram import Router, F
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile

from handlers import router

from twoversion.config import BASE_IMAGE_PATH # Импортируем путь к папке с изображениями 

# --------------------- Формулы Термодинамики  -----------------
async def send_termodinamika_formula(message: Message, filename: str, caption: str):
    try:
        image_path = os.path.join(
            BASE_IMAGE_PATH,
            "Термодинамика",
            filename
        )
        photo = FSInputFile(image_path)
        await message.answer_photo(photo, caption=caption)
    except Exception as e:
        await message.answer(f"⚠️ Ошибка загрузки формулы: {str(e)}")

@router.message(F.text == "Внутренняя энергия")
async def vnutrennyaya_energiya_handler(message: Message):
    await send_termodinamika_formula(message,
                              "Внутренняя_энергия.jpg",
                              "Понятие 'Внутренняя энергия'")
    
@router.message(F.text == "Способы теплопередачи")
async def sposobi_teploperedachi_handler(message: Message):
    await send_termodinamika_formula(message,
                              "Способы_теплопередачи.jpg",
                              "Понятие 'Способы теплопередачи'")
    
@router.message(F.text == "Количество теплоты")
async def kolichestvo_teploti_handler(message: Message):
    await send_termodinamika_formula(message,
                              "Количество_теплоты.jpg",
                              "Формула 'Количество теплоты'")
    
@router.message(F.text == "Плавление, кристаллизация")
async def plavlenie_kristallizaciya_handler(message: Message):
    await send_termodinamika_formula(message,
                              "Плавление_кристаллизация.jpg",
                              "Формула 'Плавление, кристаллизация'")
    
@router.message(F.text == "Парообразование, конденсация")
async def paroobrazovanie_kondensaciya_handler(message: Message):
    await send_termodinamika_formula(message,
                              "Парообразование_конденсация.jpg",
                              "Формула 'Парообразование, конденсация'")
    
@router.message(F.text == "Сгорание топлива")
async def sgorenie_topliva_handler(message: Message):
    await send_termodinamika_formula(message,
                              "Сгорание_топлива.jpg",
                              "Формула 'Сгорание топлива'")
    
@router.message(F.text == "Работа в термодинамике")
async def rabota_v_termodinamike_handler(message: Message):
    await send_termodinamika_formula(message,
                              "Работа_в_термодинамике.jpg",
                              "Формула 'Работа в термодинамике'")
    
@router.message(F.text == "Первый закон термодинамики")
async def perviy_zakon_termodinamiki_handler(message: Message):
    await send_termodinamika_formula(message,
                              "Первый_закон_термодинамики.jpg",
                              "Формула 'Первый закон термодинамики'")
    
@router.message(F.text == "КПД")
async def KPD_handler(message: Message):
    await send_termodinamika_formula(message,
                              "КПД.jpg",
                              "Формула 'КПД'")