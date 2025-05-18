# --------- Прямолинейное равномерное движение -----------завершено

import os
from aiogram.types import FSInputFile, Message
from aiogram import F

from twoversion.config import BASE_IMAGE_PATH # Импортируем путь к папке с изображениями 
from handlers import router

async def send_ravn_pram_dvizh_formula(message: Message, filename: str, caption: str):
    try:
        image_path = os.path.join(
            BASE_IMAGE_PATH,
            "Механика",
            "Кинематика",
            "ПрямолинейноеРавномерноеДвиж",
            filename
        )
        photo = FSInputFile(image_path)
        await message.answer_photo(photo, caption=caption)
    except Exception as e:
        await message.answer(f"⚠️ Ошибка загрузки формулы: {str(e)}")

@router.message(F.text == "Скорость прямолинейного равномерного движения")
async def send_skorost_ravn_handler(message: Message):
    await send_ravn_pram_dvizh_formula(message,
                              "скоростьПрямРавн.jpg",
                              "Формула скорости прямолинейного равномерного движения")

@router.message(F.text == "Перемещение при равномерном движении")
async def send_peremeshenie_ravn_pram_handler(message: Message):
    await send_ravn_pram_dvizh_formula(message,
                              "Перемещение_при_равномерном_прямолинейном_движении.jpg",
                              "Формула перемещения при равномерном прямолинейном движении")

@router.message(F.text == "Зависимость координаты от времени при равномерном прямолинейном движении")
async def send_kordinata_ravmomernoe_handler(message: Message):
    await send_ravn_pram_dvizh_formula(message,
                              "Зависимость_координаты_от_времени_при_равномерном_прямолинейном_движении.jpg",
                              "Формула зависимости координаты от времени при равномерном прямолинейном движении")

@router.message(F.text == "График зависимости координаты от времени при равномерном прямолинейном движении")
async def send_zavisimosy_kordinata_ravn_handler(message: Message):
    await send_ravn_pram_dvizh_formula(message,
                              "График_зависимости_координаты_от_времени_при_равномерном_прямолинейном_движении.jpg",
                              "График зависимости координаты от времени при равномерном прямолинейном движении")

@router.message(F.text == "Графики зависимости проекции скорости от времени при равномерном прямолинейном движении")
async def send_proekzia_skorosti_ravn_handler(message: Message):
    await send_ravn_pram_dvizh_formula(message,
                              "Графики_зависимости_проекции_скорости_от_времени_при_равномерном_прямолинейном_движении.jpg",
                              "Графики зависимости проекции скорости от времени при равномерном прямолинейном движении")

@router.message(F.text == "Графики зависимости проекции перемещения от времени")
async def send_grafik_zavisimost_peremeshenia_ravn_handler(message: Message):
    await send_ravn_pram_dvizh_formula(message,
                              "Графики_зависимости_проекции_перемещения_от_времени.jpg",
                              "Графики зависимости проекции перемещения от времени")


@router.message(F.text == "Графики зависимости пути от времени при равномерном прямолинейном движении")
async def send_graf_zavist_pyti_ravn_handler(message: Message):
    await send_ravn_pram_dvizh_formula(message,
                              "Графики_зависимости_пути_от_времени_при_равномерном_прямолинейном_движении.jpg",
                              "")