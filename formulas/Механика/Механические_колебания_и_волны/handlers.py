import os
from aiogram import Router, F
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile

router = Router()

from twoversion.config import BASE_IMAGE_PATH # Импортируем путь к папке с изображениями 



# --------------------- Формулы Механические колебания и волны -----------------
async def send_mechanicheskie_kolebaniya_formula(message: Message, filename: str, caption: str):
    try:
        image_path = os.path.join(
            BASE_IMAGE_PATH,
            "Механика",
            "Механические колебания и волны",
            filename
        )
        photo = FSInputFile(image_path)
        await message.answer_photo(photo, caption=caption)
    except Exception as e:
        await message.answer(f"⚠️ Ошибка загрузки формулы: {str(e)}")

@router.message(F.text == "Амплитуда колебаний")
async def amplituda_kolebaniy_handler(message: Message):
    await send_mechanicheskie_kolebaniya_formula(message,
                              "Амплитуда_колебаний.jpg",
                              "Формула амплитуды колебаний")

@router.message(F.text == "Период колебаний")
async def period_kolebaniy_handler(message: Message):
    await send_mechanicheskie_kolebaniya_formula(message,
                              "Период_колебаний.jpg",
                              "Формула периода колебаний")

@router.message(F.text == "Частота колебаний")
async def chastota_kolebaniy_handler(message: Message):
    await send_mechanicheskie_kolebaniya_formula(message,
                              "Частота_колебаний.jpg",
                              "Формула частоты колебаний")

@router.message(F.text == "Гармонические колебания")
async def garmonicheskie_kolebaniya_handler(message: Message):
    await send_mechanicheskie_kolebaniya_formula(message,
                              "Гармонические_колебания.jpg",
                              "Формула гармонических колебаний")

@router.message(F.text == "Циклическая частота")
async def ciklicheskaa_chastota_handler(message: Message):
    await send_mechanicheskie_kolebaniya_formula(message,
                              "Циклическая_частота.jpg",
                              "Формула циклической частоты")

@router.message(F.text == "Уравнение гармонических колебаний")
async def uravnenie_garmonicheskih_kolebaniy_handler(message: Message):
    await send_mechanicheskie_kolebaniya_formula(message,
                              "Уравнение_гармонических_колебаний.jpg",
                              "Формула уравнения гармонических колебаний")

@router.message(F.text == "Закон сохранения энергии для математического маятника")
async def zakon_sohraneniya_energii_matematicheskogo_mayatnika_handler(message: Message):
    await send_mechanicheskie_kolebaniya_formula(message,
                              "Закон_сохранения_энергии_для_математического_маятника.jpg",
                              "Закон сохранения энергии для математического маятника")

@router.message(F.text == "Закон сохранения энергии для пружинного маятника")
async def zakon_sohraneniya_energii_pruzhinnogo_mayatnika_handler(message: Message):
    await send_mechanicheskie_kolebaniya_formula(message,
                              "Закон_сохранения_энергии_для_пружинного_маятника.jpg",
                              "Закон сохранения энергии для пружинного маятника")

@router.message(F.text == "Период колебаний математического маятника")
async def period_kolebaniy_matematicheskogo_mayatnika_handler(message: Message):
    await send_mechanicheskie_kolebaniya_formula(message,
                              "Период_колебаний_математического_маятника.jpg",
                              "Формула периода колебаний математического маятника")

@router.message(F.text == "Период колебаний пружинного маятника")
async def period_kolebaniy_pruzhinnogo_mayatnika_handler(message: Message):
    await send_mechanicheskie_kolebaniya_formula(message,
                              "Период_колебаний_пружинного_маятника.jpg",
                              "Формула периода колебаний пружинного маятника")

@router.message(F.text == "Длина волны")
async def dlina_volny_handler(message: Message):
    await send_mechanicheskie_kolebaniya_formula(message,
                              "Длина_волны.jpg",
                              "Формула длины волны")