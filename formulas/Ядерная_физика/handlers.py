import os
from aiogram import Router, F
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile

from handlers import router

from twoversion.config import BASE_IMAGE_PATH # Импортируем путь к папке с изображениями 

# --------------------- Формулы Ядерная физика -----------------
async def send_yadernaya_fizika_formula(message: Message, filename: str, caption: str):
    try:
        image_path = os.path.join(
            BASE_IMAGE_PATH,
            "Ядерная физика",
            filename
        )
        photo = FSInputFile(image_path)
        await message.answer_photo(photo, caption=caption)
    except Exception as e:
        await message.answer(f"⚠️ Ошибка загрузки формулы: {str(e)}")

@router.message(F.text == "Массовое число")
async def massovoe_chislo_handler(message: Message):
    await send_yadernaya_fizika_formula(message,
                              "Массовое_число.jpg",
                              "Понятие 'Массовое число'")
    
@router.message(F.text == "Спектр уровней энергии атома водорода")
async def spektr_urovnej_energii_atoma_vodoroda_handler(message: Message):
    await send_yadernaya_fizika_formula(message,
                              "Спектр_уровней_энергии_атома_водорода.jpg",
                              "Формула 'Спектр уровней энергии атома водорода'")
    
@router.message(F.text == "Планетарная модель атома")
async def planetarnaya_model_atoma_handler(message: Message):
    await send_yadernaya_fizika_formula(message,
                              "Планетарная_модель_атома.jpg",
                              "Понятие 'Планетарная модель атома'")
    
@router.message(F.text == "Энергия связи")
async def energiya_svyazi_handler(message: Message):
    await send_yadernaya_fizika_formula(message,
                              "Энергия_связи.jpg",
                              "Формула 'Энергия связи'")
    
@router.message(F.text == "Изотопы")
async def izotopy_handler(message: Message):
    await send_yadernaya_fizika_formula(message,
                              "Изотопы.jpg",
                              "Понятие 'Изотопы'")
    
@router.message(F.text == "Альфа и бета распад")
async def alfa_i_beta_raspad_handler(message: Message):
    await send_yadernaya_fizika_formula(message,
                              "Альфа_и_бета_распад.jpg",
                              "Формула 'Альфа и бета распад'")
    
@router.message(F.text == "Обозначение атомного ядра")
async def oboznachenie_atomnogo_yadra_handler(message: Message):
    await send_yadernaya_fizika_formula(message,
                              "Обозначение_атомного_ядра.jpg",
                              "Формула 'Обозначение атомного ядра'")
    
@router.message(F.text == "Дефект массы ядра")
async def defekt_massi_yadra_handler(message: Message):
    await send_yadernaya_fizika_formula(message,
                              "Дефект_массы_ядра.jpg",
                              "Формула 'Дефект массы ядра'")
    
@router.message(F.text == "Закон радиоактивного распада")
async def zakon_radioaktivnogo_raspada_handler(message: Message):
    await send_yadernaya_fizika_formula(message,
                              "Закон_радиоактивного_распада.jpg",
                              "Формула 'Закон радиоактивного распада'")
    
@router.message(F.text == "Масса фотона")
async def massa_fotona_handler(message: Message):
    await send_yadernaya_fizika_formula(message,
                              "Масса_фотона.jpg",
                              "Формула 'Масса фотона'")