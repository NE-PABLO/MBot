import os
from aiogram import F
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile

from handlers import router

from twoversion.config import BASE_IMAGE_PATH # Импортируем путь к папке с изображениями 


# --------------------- Формулы Магнитное поле и электромагнитная индукция -----------------
async def send_magnetic_field_formula(message: Message, filename: str, caption: str):
    try:
        image_path = os.path.join(
            BASE_IMAGE_PATH,
            "Электродинамика",
            "Магнитное поле и электромагнитная индукция",
            filename
        )
        photo = FSInputFile(image_path)
        await message.answer_photo(photo, caption=caption)
    except Exception as e:
        await message.answer(f"⚠️ Ошибка загрузки формулы: {str(e)}")

@router.message(F.text == "Линии магнитной индукции")
async def linii_magnitnoy_indukcii_handler(message: Message):
    await send_magnetic_field_formula(message,
                              "Линии_магнитной_индукции.jpg",
                              "Понятие 'Линии магнитной индукции'")
    
@router.message(F.text == "Графическое представление магнитного поля")
async def graficheskoe_predstavlenie_magnitnogo_polya_handler(message: Message):
    await send_magnetic_field_formula(message,
                              "Графическое_представление_магнитного_поля.jpg",
                              "Понятие 'Графическое представление магнитного поля'")
    
@router.message(F.text == "Правило правой руки или правило буравчика")
async def pravilo_pravoy_ruki_handler(message: Message):
    await send_magnetic_field_formula(message,
                              "Правило_правой_руки_или_правило_буравчика.jpg",
                              "Понятие 'Правило правой руки или правило буравчика'")
    
@router.message(F.text == "Сила Ампера")
async def sila_ampera_handler(message: Message):
    await send_magnetic_field_formula(message,
                              "Сила_Ампера.jpg",
                              "Формула силы Ампера")
    
@router.message(F.text == "Правило левой руки")
async def pravilo_levoi_ruki_handler(message: Message):
    await send_magnetic_field_formula(message,
                              "Правило_левой_руки.jpg",
                              "Понятие 'Правило левой руки'")
    
@router.message(F.text == "Сила Лоренца")
async def sila_lorenca_handler(message: Message):
    await send_magnetic_field_formula(message,
                              "Сила_Лоренца.jpg",
                              "Формула силы Лоренца")
    
@router.message(F.text == "Явление электромагнитной индукции")
async def yavlenie_electromagnitnoy_indukcii_handler(message: Message):
    await send_magnetic_field_formula(message,
                              "Явление_электромагнитной_индукции.jpg",
                              "Понятие 'Явление электромагнитной индукции'")
    
@router.message(F.text == "Поток вектора магнитной индукции")
async def potok_vektora_magnitnoy_indukcii_handler(message: Message):
    await send_magnetic_field_formula(message,
                              "Поток_вектора_магнитной_индукции.jpg",
                              "Формула потока вектора магнитной индукции")

@router.message(F.text == "Закон электромагнитной индукции Фарадея")
async def zakon_electromagnitnoy_indukcii_faradeya_handler(message: Message):
    await send_magnetic_field_formula(message,
                              "Закон_электромагнитной_индукции_Фарадея.jpg",
                              "Формула закона электромагнитной индукции Фарадея")
    
@router.message(F.text == "ЭДС индукции в прямом проводнике, движущемся в магнитном поле")
async def eds_indukcii_v_pramom_provodnike_handler(message: Message):
    await send_magnetic_field_formula(message,
                              "ЭДС_индукции_в_прямом_проводнике,_движущемся_в_магнитном_поле.jpg",
                              "Формула ЭДС индукции в прямом проводнике, движущемся в магнитном поле")
    
@router.message(F.text == "Индуктивность")
async def induktivnost_handler(message: Message):
    await send_magnetic_field_formula(message,
                              "Индуктивность.jpg",
                              "Формула индуктивности")
    
@router.message(F.text == "ЭДС самоиндукции")
async def eds_samoinduktsii_handler(message: Message):
    await send_magnetic_field_formula(message,
                              "ЭДС_самоиндукции.jpg",
                              "Формула ЭДС самоиндукции")