import os
from aiogram import F
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile

from handlers import router

from twoversion.config import BASE_IMAGE_PATH # Импортируем путь к папке с изображениями 

# --------------------- Формулы Электрическое поле -----------------
async def send_electric_field_formula(message: Message, filename: str, caption: str):
    try:
        image_path = os.path.join(
            BASE_IMAGE_PATH,
            "Электродинамика",
            "Электрическое поле",
            filename
        )
        photo = FSInputFile(image_path)
        await message.answer_photo(photo, caption=caption)
    except Exception as e:
        await message.answer(f"⚠️ Ошибка загрузки формулы: {str(e)}")

@router.message(F.text == "Закон Кулона")
async def zakon_kulona_handler(message: Message):
    await send_electric_field_formula(message,
                              "Закон_Кулона.jpg",
                              "Формула закона Кулона")
    
@router.message(F.text == "Напряженность электрического поля")
async def napryazhennost_electric_field_handler(message: Message):
    await send_electric_field_formula(message,
                              "Напряженность_электрического_поля.jpg",
                              "Формула напряженности электрического поля")
    
@router.message(F.text == "Напряженность поля точечного заряда")
async def napryazhennost_pole_tochechnogo_zaryada_handler(message: Message):
    await send_electric_field_formula(message,
                              "Напряженность_поля_точечного_заряда.jpg",
                              "Формула напряженности поля точечного заряда")
    
@router.message(F.text == "Потенциал точки электростатического поля")
async def potencial_tochki_electrostaticheskogo_pole_handler(message: Message):
    await send_electric_field_formula(message,
                              "Потенциал_точки_электростатического_поля.jpg",
                              "Формула потенциала точки электростатического поля")
    
@router.message(F.text == "Разность потенциалов (напряжение)")
async def raznost_potencialov_napryazhenie_handler(message: Message):
    await send_electric_field_formula(message,
                              "Разность_потенциалов_(напряжение).jpg",
                              "Формула разности потенциалов (напряжение)")
    
@router.message(F.text == "Электроёмкость")
async def electroemkost_handler(message: Message):
    await send_electric_field_formula(message,
                              "Электроёмкость.jpg",
                              "Формула электроёмкости")
    
@router.message(F.text == "Соединение конденсаторов (параллельное/последовательное)")
async def soedinenie_kondensatorov_handler(message: Message):
    await send_electric_field_formula(message,
                              "Соединение_конденсаторов_(параллельноепоследовательное).jpg",
                              "Формула соединения конденсаторов (параллельное/последовательное)")
    
@router.message(F.text == "Энергия заряженного конденсатора")
async def energiya_zaryajennogo_kondensatora_handler(message: Message):
    await send_electric_field_formula(message,
                              "Энергия_заряженного_конденсатора.jpg",
                              "Формула энергии заряженного конденсатора")