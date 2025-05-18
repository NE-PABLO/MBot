import os
from aiogram import F
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile

from handlers import router # Импортируем роутер из файла handlers.py

from twoversion.config import BASE_IMAGE_PATH # Импортируем путь к папке с изображениями 

# --------------------- Формулы Молекулярной физики  -----------------

async def send_molekularnaya_fizika_formula(message: Message, filename: str, caption: str):
    try:
        image_path = os.path.join(
            BASE_IMAGE_PATH,
            "Молекулярная физика",
            filename
        )
        photo = FSInputFile(image_path)
        await message.answer_photo(photo, caption=caption)
    except Exception as e:
        await message.answer(f"⚠️ Ошибка загрузки формулы: {str(e)}")


@router.message(F.text == "Количество вещества")
async def kolichestvo_veshestva_handler(message: Message):
    await send_molekularnaya_fizika_formula(message,
                              "Количество_вещества.jpg",
                              "Понятие 'Количество вещества'")
    
@router.message(F.text == "Основные положения МКТ")
async def osnovnie_polozheniya_MKT_handler(message: Message):
    await send_molekularnaya_fizika_formula(message,
                              "Основные_положения_МКТ.jpg",
                              "Понятие 'Основные положения МКТ'")
    
@router.message(F.text == "Диффузия")
async def diffuziya_handler(message: Message):
    await send_molekularnaya_fizika_formula(message,
                              "Диффузия.jpg",
                              "Понятие 'Диффузия'")
    
@router.message(F.text == "Идеальный газ")
async def idealniy_gaz_handler(message: Message):
    await send_molekularnaya_fizika_formula(message,
                              "Идеальный_газ.jpg",
                              "Понятие 'Идеальный газ'")
    
@router.message(F.text == "Основное уравнение МКТ идеального газа")
async def osnovnoe_uravnenie_MKT_ideal(message: Message):
    await send_molekularnaya_fizika_formula(message,
                              "Основное_уравнение_МКТ_идеального_газа.jpg",
                              "Формула 'Основное уравнение МКТ идеального газа'")
    
@router.message(F.text == "Связь температуры газа со средней кинетической энергией")
async def svyaz_temperaturi_gas_sred_kinet_energiy_handler(message: Message):
    await send_molekularnaya_fizika_formula(message,
                              "Связь_температуры_газа_со_средней_кинетической_энергией.jpg",
                              "Формула 'Связь температуры газа со средней кинетической энергией'")
    
@router.message(F.text == "Уравнение Менделеева-Клапейрона")
async def uravnenie_Mendeleeva_Klapeyrona_handler(message: Message):
    await send_molekularnaya_fizika_formula(message,
                              "Уравнение_Менделеева-Клапейрона.jpg",
                              "Формула 'Уравнение Менделеева-Клапейрона'")
    
@router.message(F.text == "Внутренняя энергия одноатомного идеального газа")
async def vnutrennyaya_energiya_odnoatomnogo_idealnogo_gaza_handler(message: Message):
    await send_molekularnaya_fizika_formula(message,
                              "Внутренняя_энергия_одноатомного_идеального_газа.jpg",
                              "Формула 'Внутренняя энергия одноатомного идеального газа'")
    
@router.message(F.text == "Изотермический процесс")
async def izotermicheskiy_process_handler(message: Message):
    await send_molekularnaya_fizika_formula(message,
                              "Изотермический_процесс.jpg",
                              "Формула 'Изотермический процесс'")
    
@router.message(F.text == "Закон Дальтона")
async def zakon_Daltona_handler(message: Message):
    await send_molekularnaya_fizika_formula(message,
                              "Закон_Дальтона.jpg",
                              "Формула 'Закон Дальтона'")

@router.message(F.text == "Насыщенный пар")
async def nasichenniy_par_handler(message: Message):
    await send_molekularnaya_fizika_formula(message,
                              "Насыщенный_пар.jpg",
                              "Понятие 'Насыщенный пар'")
    
@router.message(F.text == "Абсолютная влажность")
async def absolutnaya_vlazhnost_handler(message: Message):
    await send_molekularnaya_fizika_formula(message,
                              "Абсолютная_влажность.jpg",
                              "Формула 'Абсолютная влажность'")

@router.message(F.text == "Относительная влажность")
async def otnositelnaya_vlazhnost_handler(message: Message):
    await send_molekularnaya_fizika_formula(message,
                              "Относительная_влажность.jpg",
                              "Формула 'Относительная влажность'")